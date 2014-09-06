import io
 
file_ = open('build_def.txt', 'w')
lines = ['[Details]\n',
'name = test\n',
'\n',
'[Packages]\n',
'Linux = 3.10\n',
'\n'
]
file_.writelines(lines)
file_.close(),
