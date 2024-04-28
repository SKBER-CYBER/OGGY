import os,time
S = '\033[1;37m';A = '\x1b[38;5;208m';R = '\x1b[38;5;46m';F = '\x1b[38;5;48m';Z = '\033[1;33m';A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;48m';h = '\x1b[38;5;48m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';W = '\x1b[38;5;196m';hh = '\033[34;1m'
logo=f"""{G1}
{A}MM    MM RRRRRR      OOOOO    GGGG    GGGG  YY   YY  {G1}J
{G1}MMM  MMM RR   RR    OO   OO  GG  GG  GG  GG YY   YY  {R}A
{A}MM MM MM RRRRRR     OO   OO GG      GG       YYYYY   {X3}H
{G1}MM    MM RR  RR     OO   OO GG   GG GG   GG   YYY    {Y}I
{A}MM    MM RR   RR     OOOO0   GGGGGG  GGGGGG   YYY    {X1}D    
{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{A}[{G1}+{A}]{G1} DEVELOPER  {G1}━{R}>{G1} MR{Y}/{G1}OGGY
{A}[{G1}+{A}]{G1} GITHUB     {G1}━{R}>{G1} SKBER{Y}-{G1}CYBER
{A}[{G1}+{A}]{G1} TOOLS      {G1}━{R}>{G1} RANDOM{Y}/{G1}FILE
{A}[{G1}+{A}]{G1} VERSION    {G1}━{R}>{G1} V{Y}/{G1}12 {R}({G1}={Y}PREMIUM{G1}={R})
{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
os.system('clear')
print(logo)
for up in range(10):
  print(f"{A}[{G1}+{A}] PLEASE WAIT YOUR NEXT UPDATE ")
  time.sleep(1)
