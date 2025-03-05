set autoindent
set backspace=indent,eol,start
set cindent
set confirm
set expandtab
set foldlevel=99
set foldmethod=indent
set history=1000
set hlsearch
set incsearch
set laststatus=2
set mouse-=a
set number
set ruler
set shiftround
set shiftwidth=2
set showmatch
set smartcase
set smartindent
set smarttab
syntax on
set tabstop=2
set title
set wrap
filetype indent plugin on
syntax enable
nnoremap <return><return> :noh<return><esc>
" automatically strip whitespace off the end of lines on save
autocmd BufWritePre *.py :%s/\s\+$//e
