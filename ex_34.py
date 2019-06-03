from time import sleep

x = 0.05

things = (
"e                                   ",
"ee                                  ",
"uee                                 ",
"quee                                ",
"rquee                               ",
"arquee                              ",
"marquee                             ",
" marquee                            ",
"  marquee                           ",
"   marquee                          ",
"    marquee                         ",
"     marquee                        ",
"      marquee                       ",
"       marquee                      ",
"        marquee                     ",
"         marquee                    ",
"          marquee                   ",
"           marquee                  ",
"            marquee                 ",
"             marquee                ",
"              marquee               ",
"               marquee              ",
"                marquee             ",
"                 marquee            ",
"                  marquee           ",
"                   marquee          ",
"                    marquee         ",
"                     marquee        ",
"                      marquee       ",
"                       marquee      ",
"                        marquee     ",
"                         marquee    ",
"                          marquee   ",
"                           marquee  ",
"                            marquee ",
"                             marquee",
"                              marque",
"                               marqu",
"                                marq",
"                                 mar",
"                                  ma",
"                                   m",
"                                    "
)

while True:
    for i in things:    
        print(i)
        sleep(x)
        print("\33[2A")
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
print(line.rstrip())

