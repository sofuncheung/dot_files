colorscheme torte 
set modeline
set modelines=5
:set tabstop=4
:set shiftwidth=4
:set expandtab
:retab
set autoindent
" I think I prefer maunal folding 
:set foldmethod=manual
nnoremap <silent> <Space> @=(foldlevel('.')?'za':"\<Space>")<CR>
vnoremap <Space> zf
