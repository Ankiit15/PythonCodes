from time import sleep

x = 0.05

qwerty = (
"e                              ",
"ae                             ",
"tae                            ",
" tae                           ",
"  tae                          ",
"   tae                         ",
"    tae                        ",
"     tae                       ",
"      tae                      ",
"       tae                     ",
"        tae                    ",
"         tae                   ",
"          tae                  ",
"           tae                 ",
"            tae                ",
"             tae               ",
"              tae              ",
"               tae             ",
"                tae            ",
"                 tae           ",
"                  tae          ",
"                   tae         ",
"                    tae        ",
"                     tae       ",
"                      tae      ",
"                       tae     ",
"                        tae    ",
"                         tae   ",
"                          tae  ",
"                           tae ",
"                            tae",
"                             ta",
"                              t",
"                               ",
)


while True:
    for i in qwerty:    
        print(i)
        sleep(x)
        print("\33[2A")
