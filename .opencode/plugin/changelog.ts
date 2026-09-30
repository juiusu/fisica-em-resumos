import { mkdir, readFile, writeFile } from "node:fs/promises"
import { dirname, isAbsolute, join, relative } from "node:path"
import type { Plugin } from "@opencode-ai/plugin"

const CHANGELOG = "CHANGELOG.org"

const IGNORED = [
  /^\.git(\/|$)/,
  /^\.packages(\/|$)/,
  /^public(\/|$)/,
  /^\.opencode(\/|$)/,
  /^CHANGELOG\.org$/,
]

function pad(n: number): string {
  return String(n).padStart(2, "0")
}

export default (async ({ directory }) => {
  const changelog = join(directory, CHANGELOG)

  return {
    event: async ({ event }) => {
      if (event.type !== "file.edited") return
      const raw = event.properties?.file
      if (!raw) return

      const abs = isAbsolute(raw) ? raw : join(directory, raw)
      const rel = relative(directory, abs).split("\\").join("/")
      if (rel.startsWith("..") || IGNORED.some((re) => re.test(rel))) return

      const now = new Date()
      const day = `${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())}`
      const time = `${pad(now.getHours())}:${pad(now.getMinutes())}`
      const heading = `* ${day}`
      const entry = `- editado: ${rel} (${time})`

      await mkdir(dirname(changelog), { recursive: true })
      let content = ""
      try {
        content = await readFile(changelog, "utf8")
      } catch {
        content = ""
      }

      const start = content.indexOf(heading)
      if (start !== -1) {
        const next = content.indexOf("\n* ", start + 1)
        const section = next === -1 ? content.slice(start) : content.slice(start, next)
        if (section.includes(`- editado: ${rel} (`)) return
        content = content.slice(0, start + heading.length) + `\n${entry}` + content.slice(start + heading.length)
      } else {
        content = `${content.trimEnd()}\n\n${heading}\n${entry}\n`
      }

      await writeFile(changelog, content, "utf8")
    },
  }
}) satisfies Plugin
