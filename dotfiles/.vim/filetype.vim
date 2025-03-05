    " my filetype file
    if exists("did_load_filetypes")
        finish
    endif
    augroup filetypedetect
        au! BufRead,BufNewFile *.aurora         setfiletype python
        au! BufRead,BufNewFile *.workflow       setfiletype json
    augroup END
