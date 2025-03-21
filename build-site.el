
;; this is my configuration emacs file for export org mode files to html . Hoe can I add a figura png that is in my conent folder in the index.org so that the index.htm show the figure correctnly ?


;; Set the package installation directory so that packages aren't stored in the
;; ~/.emacs.d/elpa path.
(require 'package)
(setq package-user-dir (expand-file-name "./.packages"))
(setq package-archives '(("melpa" . "https://melpa.org/packages/")
                         ("elpa" . "https://elpa.gnu.org/packages/")))

;; Initialize the package system
(package-initialize)
(unless package-archive-contents
  (package-refresh-contents))

;; Install dependencies
(package-install 'htmlize)

;; Load the publishing system
(require 'ox-publish)

(org-publish-all t)
(image-type-available-p 'png)



;; Customize the HTML output
(setq org-html-validation-link nil            ;; Don't show validation link
      org-html-head-include-scripts nil       ;; Use our own scripts
      org-html-head-include-default-style nil ;; Use our own styles
      org-html-head "<link rel=\"stylesheet\" href=\"https://cdn.simplecss.org/simple.min.css\" />"
      org-html-head "<meta http-equiv=\"Content-Language\" content=\"pt-BR\">\n
                     <link rel=\"stylesheet\" href=\"https://cdn.simplecss.org/simple.min.css\" />")



;; traduções - VERIFICAR POR QUE NÃO ESTÁ TRADUZINDO
;; ORG

(setq org-export-dictionary
      '(
        (pt-BR  ; Language code
	 ("Table of Contents" . "Índice")
         ("Author" . "Autor")
         ("Date" . "Data")
	 ("Figure" . "Figura")
	 ("Table" . "Tabela")
	 )
        ))

;;HTML 

(setq org-html-element-dictionary
      '(
        (pt-BR
         ("Table of Contents" . "Índice")
         ("Author" . "Autor")
         ("Date" . "Data")
	 ("Figure" . "Figura")
	 ("Table" . "Tabela")
         )
        ))

;; Define the publishing project
(setq org-publish-project-alist
      (list
       (list "fisica-em-resumos"
             :recursive t
             :base-directory "./content"
             :publishing-function 'org-html-publish-to-html
             :publishing-directory "./public"
             :with-author t
	     :with-email t
	     :email "joilson.porto@ifam.edu.br"
	     :author "Joilson Silva Porto"
             :language "pt-BR"
             :with-creator t            ;; Include Emacs and Org versions in footer
             :with-toc nil                ;; Don't include a table of contents
             :section-numbers nil       ;; Don't include section numbers
             :time-stamp-file nil)))    ;; Don't include time stamp in file

;; Generate the site output
(org-publish-all t)

(message "Build complete!")
