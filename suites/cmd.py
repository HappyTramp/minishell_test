# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    cmd.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: charles <charles.cabergs@gmail.com>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/07/15 15:11:46 by charles           #+#    #+#              #
#    Updated: 2020/07/15 18:21:56 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import distutils

import config
from suite import suite


@suite
def suite_redirection(test):
    test("echo bonjour > test", setup="", files=["test"])
    test("echo > test bonjour", setup="", files=["test"])
    test("> test echo bonjour", setup="", files=["test"])
    test("echo bonjour >> test", setup="", files=["test"])
    test("echo >> test bonjour", setup="", files=["test"])
    test(">> test echo bonjour", setup="", files=["test"])
    test("cat < test", setup="echo bonjour > test")
    test("echo bonjour > test", setup="", files=["test"])

    test("echo > test'sticked' bonjour", setup="", files=["teststicked"])
    test("> test'sticked' echo bonjour", setup="", files=["teststicked"])
    test("echo bonjour >> test'sticked'", setup="", files=["teststicked"])
    test("echo >> test'sticked' bonjour", setup="", files=["teststicked"])
    test(">> test'sticked' echo bonjour", setup="", files=["teststicked"])
    test("cat < test'sticked'", setup="echo bonjour > test'sticked'")
    test("< test'sticked' cat", setup="echo bonjour > test'sticked'")

    test("echo > test\"sticked\" bonjour", setup="", files=["teststicked"])
    test("> test\"sticked\" echo bonjour", setup="", files=["teststicked"])
    test("echo bonjour >> test\"sticked\"", setup="", files=["teststicked"])
    test("echo >> test\"sticked\" bonjour", setup="", files=["teststicked"])
    test(">> test\"sticked\" echo bonjour", setup="", files=["teststicked"])
    test("cat < test\"sticked\"", setup="echo bonjour > test\"sticked\"")
    test("< test\"sticked\" cat", setup="echo bonjour > test\"sticked\"")

    test("echo > test'yo'\"sticked\" bonjour", setup="", files=["testyosticked"])
    test("> test'yo'\"sticked\" echo bonjour", setup="", files=["testyosticked"])
    test("echo bonjour >> test'yo'\"sticked\"", setup="", files=["testyosticked"])
    test("echo >> test'yo'\"sticked\" bonjour", setup="", files=["testyosticked"])
    test(">> test'yo'\"sticked\" echo bonjour", setup="", files=["testyosticked"])
    test("cat < test'yo'\"sticked\"", setup="echo bonjour > test'yo'\"sticked\"")
    test("< test'yo'\"sticked\" cat", setup="echo bonjour > test'yo'\"sticked\"")

    test("echo bonjour > test > je > suis", setup="", files=["test", "je", "suis"])
    test("echo > test > je bonjour > suis", setup="", files=["test", "je", "suis"])
    test("> test echo bonjour > je > suis", setup="", files=["test", "je", "suis"])
    test("echo bonjour >> test > je >> suis", setup="", files=["test", "je", "suis"])
    test("echo >> test bonjour > je > suis", setup="", files=["test", "je", "suis"])
    test(">> test echo > je bonjour > suis", setup="", files=["test", "je", "suis"])
    test("cat < test < je", setup="echo bonjour > test; echo salut > je")

    test("echo bonjour>test>je>suis", setup="", files=["test", "je", "suis"])
    test(">test echo bonjour>je>suis", setup="", files=["test", "je", "suis"])
    test("echo bonjour>>test>je>>suis", setup="", files=["test", "je", "suis"])
    test("cat<test<je", setup="echo bonjour > test; echo salut > je")

    test("echo bonjour > a'b'c'd'e'f'g'h'i'j'k'l'm'n'o'p'q'r's't'u'v'w'x'y'z'",
            files=["abcdefghijklmnopqrstuvwxyz"])
    test('echo bonjour > a"b"c"d"e"f"g"h"i"j"k"l"m"n"o"p"q"r"s"t"u"v"w"x"y"z"',
            files=["abcdefghijklmnopqrstuvwxyz"])
    test('echo bonjour > a\'b\'c"d"e\'f\'g"h"i\'j\'k"l"m\'n\'o"p\'q\'r"s\'t\'u"v"w"x"y\'z\'',
            files=["abcdefghijklmnopqrstuvwxyz"])

    test("> file", files=["file"])
    test("< file", setup="echo bonjour > file")

@suite
def suite_edgecases(test):
    test('echo "\\"" >>a"b""c"  ', files=["abc"])
    test("echo " + ''.join([chr(i) for i in range(1, 127) if chr(i) not in '\n`"\'()|&><']))
    test("echo foo>bar", files=["bar"])
    test("echo foo >bar", files=["bar"])
    test("echo foo> bar", files=["bar"])
    test("echo foo > bar", files=["bar"])

@suite
def suite_cmd_error(test):
    test(">")
    test(">>")
    test("<")
    test("echo >")
    test("echo >>")
    test("echo <")

    test("> test", files=["test"])
    test(">> test", files=["test"])
    test("< test", setup="touch test")

    test("echo foo >>> bar")
    test("echo foo >>>> bar")
    test("echo foo >>>>> bar")

    test("cat <<< bar", setup="echo bonjour > bar")
    test("cat <<<< bar", setup="echo bonjour > bar")
    test("cat <<<<< bar", setup="echo bonjour > bar")

    test("notfound")
    test("notfound a b c")

@suite
def suite_cmd_variable(test):
    test("A=a bash -c 'echo $A'")
    test("A=a B=b bash -c 'echo $A$B'")
    test("A=a B=b C=c D=d E=e F=f G=g H=h bash -c 'echo $A$B$C$D$E$F$G$H'")
    test("A=a A=bonjour bash -c 'echo $A'")
    test("A=aA=bonjour bash -c 'echo $A'")
    test("BONJOURJESUIS=a bash -c 'echo $BONJOURJESUIS'")
    test("bonjourjesuis=a bash -c 'echo $bonjourjesuis'")
    test("bonjour_je_suis=a bash -c 'echo $bonjour_je_suis'")
    test("BONJOURJESUIS1=a bash -c 'echo $BONJOURJESUIS1'")
    test("bO_nJq123o__1ju_je3234sui__a=a bash -c 'echo $bO_nJq123o__1ju_je3234sui__a'")
    test("a0123456789=a bash -c 'echo $a0123456789")
    test("abcdefghijklmnopqrstuvwxyz=a bash -c 'echo $abcdefghijklmnopqrstuvwxyz'")
    test("ABCDEFGHIJKLMNOPQRSTUVWXYZ=a bash -c 'echo $ABCDEFGHIJKLMNOPQRSTUVWXYZ'")
    test("__________________________=a bash -c 'echo $__________________________'")
    test("_bonjour_=a bash -c 'echo $_bonjour_'")
    test("_=a bash -c 'echo $_a'")
    test("1=a bash -c 'echo $1'")
    test("BONJOURJESUIS =a bash -c 'echo $BONJOURJESUIS '")
    test("BONJOURJESUIS= a bash -c 'echo $BONJOURJESUIS'")
    test(r"BONJOUR\\JESUIS=a bash -c 'echo $BONJOUR\\JESUIS'")
    test(r"BONJOUR\'JESUIS=a bash -c 'echo $BONJOUR\'JESUIS'")
    test(r'BONJOUR\"JESUIS=a bash -c "echo $BONJOUR\"JESUIS"')
    test(r"BONJOUR\$JESUIS=a bash -c 'echo $BONJOUR\$JESUIS'")
    test(r"BONJOUR\&JESUIS=a bash -c 'echo $BONJOUR\&JESUIS'")
    test(r"BONJOUR\|JESUIS=a bash -c 'echo $BONJOUR\|JESUIS'")
    test(r"BONJOUR\;JESUIS=a bash -c 'echo $BONJOUR\;JESUIS'")
    test(r"BONJOUR\_JESUIS=a bash -c 'echo $BONJOUR\_JESUIS'")
    test(r"BONJOUR\0JESUIS=a bash -c 'echo $BONJOUR\0JESUIS'")
    test(r"\B\O\N\ \ \ \ \ \ \ JOURJESUIS=a bash -c 'echo $\B\O\N\ \ \ \ \ \ \ JOURJESUIS'")
    test(r"A=\B\O\N\ \ \ \ \ \ \ JOURJESUIS bash -c 'echo $A'")
    test(r"A='bonjour je suis charles' bash -c 'echo $A'")
    test(r'A="bonjour je suis charles" bash -c "echo $A"')
    test(r"A==a bash -c 'echo $A'")
    test(r"A===a bash -c 'echo $A'")
    test(r"A====a bash -c 'echo $A'")
    test(r"A=====a bash -c 'echo $A'")
    test(r"A======a bash -c 'echo $A'")
    test(r"A=a=a=a=a=a bash -c 'echo $A'")

    test("A=a; echo $A")
    test("A=a B=b; echo $A$B")
    test("A=a B=b C=c D=d E=e F=f G=g H=h; echo $A$B$C$D$E$F$G$H")
    test("A=a A=bonjour; echo $A")
    test("A=aA=bonjour; echo $A")
    test("BONJOURJESUIS=a; echo $BONJOURJESUIS")
    test("bonjourjesuis=a; echo $bonjourjesuis")
    test("bonjour_je_suis=a; echo $bonjour_je_suis")
    test("BONJOURJESUIS1=a; echo $BONJOURJESUIS1")
    test("bO_nJq123o__1ju_je3234sui__a=a; echo $bO_nJq123o__1ju_je3234sui__a")
    test("a0123456789=a; echo $a0123456789")
    test("abcdefghijklmnopqrstuvwxyz=a; echo $abcdefghijklmnopqrstuvwxyz")
    test("ABCDEFGHIJKLMNOPQRSTUVWXYZ=a; echo $ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    test("__________________________=a; echo $__________________________")
    test("_bonjour_=a; echo $_bonjour_")
    test("_=a; echo $_a")
    test("1=a; echo $1")
    test("BONJOURJESUIS =a; echo $BONJOURJESUIS ")
    test("BONJOURJESUIS= a; echo $BONJOURJESUIS")
    test(r"BONJOUR\\JESUIS=a; echo $BONJOUR\\JESUIS")
    test(r"BONJOUR\'JESUIS=a; echo $BONJOUR\'JESUIS")
    test(r'BONJOUR\"JESUIS=a; echo $BONJOUR\"JESUIS')
    test(r"BONJOUR\$JESUIS=a; echo $BONJOUR\$JESUIS")
    test(r"BONJOUR\&JESUIS=a; echo $BONJOUR\&JESUIS")
    test(r"BONJOUR\|JESUIS=a; echo $BONJOUR\|JESUIS")
    test(r"BONJOUR\;JESUIS=a; echo $BONJOUR\;JESUIS")
    test(r"BONJOUR\_JESUIS=a; echo $BONJOUR\_JESUIS")
    test(r"BONJOUR\0JESUIS=a; echo $BONJOUR\0JESUIS")
    test(r"\B\O\N\ \ \ \ \ \ \ JOURJESUIS=a; echo $\B\O\N\ \ \ \ \ \ \ JOURJESUIS")
    test(r"A=\B\O\N\ \ \ \ \ \ \ JOURJESUIS; echo $A")
    test(r"A='bonjour je suis charles'; echo $A")
    test(r'A="bonjour je suis charles"; echo $A')
    test(r"A==a; echo $A")
    test(r"A===a; echo $A")
    test(r"A====a; echo $A")
    test(r"A=====a; echo $A")
    test(r"A======a; echo $A")
    test(r"A=a=a=a=a=a; echo $A")

    test("PATH=a ls")
    test("PATH=a echo aa")
    test("A=a echo $A")
    test("A=a B=b echo $A$B")
    test("A=a B=b C=c D=d E=e F=f G=g H=h echo $A$B$C$D$E$F$G$H")
    test("A=$PATH bash -c 'echo $A'")
    test("A=\"$PATH je  suis\" bash -c 'echo $A'")
    test("A='$PATH je  suis' bash -c 'echo $A'")
    test("$TEST bash -c 'echo $A'", setup="export TEST='A=a'")

@suite
def suite_cmd_path(test):
    ls_path = distutils.spawn.find_executable("ls")
    cat_path = distutils.spawn.find_executable("cat")

    test(ls_path, setup="touch a b c")
    test(ls_path + " -l", setup="touch a b c")
    test("./bonjour", setup="touch a b c; cp {} bonjour".format(ls_path))
    test("./bonjour -l", setup="touch a b c; cp {} bonjour".format(ls_path))
    test("./somedir/bonjour -l",
            setup="mkdir somedir; touch a b c; touch somedir/d somedir/e;" +
                  "cp {} somedir/bonjour".format(ls_path))

    test("./ls . a b c",
            setup="touch a b c; echo bonjour > a; cp {} ls".format(cat_path))
    test("ls . a b c",
            setup="touch a b c; echo bonjour > a; cp {} ls".format(cat_path))
