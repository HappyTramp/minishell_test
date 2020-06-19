import config
from suite import suite

@suite
def suite_echo(test):
    test("echo bonjour")
    test("echo lalalala lalalalal alalalalal alalalala")
    test("echo lalalala                lalalalal      alalalalal alalalala")
    test("echo " + config.LOREM)

    test("echo -n bonjour")
    test("echo -n lalalala lalalalal alalalalal alalalala")
    test("echo -n lalalala                lalalalal      alalalalal alalalala")
    test("echo -n " + config.LOREM)

@suite
def suite_export(test):
    test("export A=a; echo $A")
    test("export A=a B=b C=c; echo $A$B$C")
    test("export A=a B=b C=c D=d E=e F=f G=g H=h I=i J=j K=k L=l" +
            "M=m N=n O=o P=p Q=q R=r S=s T=t U=u V=v W=w X=x Y=y Z=z" +
            "; echo $A$B$C$D$E$F$G$H$I$J$K$L$M$N$O$P$Q$R$S$T$U$V$W$X$Y$Z")
    test("export BONJOURJESUIS=a; echo $BONJOURJESUIS")
    test("export bonjourjesuis=a; echo $bonjourjesuis")
    test("export bonjour_je_suis=a; echo $bonjour_je_suis")
    test("export BONJOURJESUIS1=a; echo $BONJOURJESUIS1")
    test("export bO_nJq123o__1ju_je3234sui__a=a; echo $bO_nJq123o__1ju_je3234sui__a")
    test("export a0123456789=a; echo $a0123456789")
    test("export abcdefghijklmnopqrstuvwxyz=a; echo $abcdefghijklmnopqrstuvwxyz")
    test("export ABCDEFGHIJKLMNOPQRSTUVWXYZ=a; echo $ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    test("export __________________________=a; echo $__________________________")
    test("export _bonjour_=a; echo $_bonjour_")
    test("export _=a; echo $_a")
    test("export 1=a")
    test("export BONJOURJESUIS =a")
    test("export BONJOURJESUIS= a")
    test(r"export BONJOUR\\JESUIS=a")
    test(r"export BONJOUR\'JESUIS=a")
    test(r'export BONJOUR\"JESUIS=a')
    test(r"export BONJOUR\$JESUIS=a")
    test(r"export BONJOUR\&JESUIS=a")
    test(r"export BONJOUR\|JESUIS=a")
    test(r"export BONJOUR\;JESUIS=a")
    test(r"export BONJOUR\_JESUIS=a")
    test(r"export BONJOUR\0JESUIS=a")
    test(r"export \B\O\N\ \ \ \ \ \ \ JOURJESUIS=a")
    test(r"export A=\B\O\N\ \ \ \ \ \ \ JOURJESUIS; echo $A")
    test(r"export A='bonjour je suis charles'; echo $A")
    test(r'export A="bonjour je suis charles"; echo $A')
    test(r"export A==a; echo $A")
    test(r"export A===a; echo $A")
    test(r"export A====a; echo $A")
    test(r"export A=====a; echo $A")
    test(r"export A======a; echo $A")
    test(r"export A=a=a=a=a=a; echo $A")

@suite
def suite_cd(test):
    test("cd .; pwd");
    test("cd ..; pwd");
    test("cd ../..; pwd");
    test("cd ../../..; pwd");
    test("cd ../../../..; pwd");
    test("cd ../../../../..; pwd");
    test("cd ../../../../../..; pwd");
    test("cd /; pwd");
    test("cd /etc; pwd");
    test("cd $HOME; pwd");
    test("cd ~; pwd");

@suite
def suite_unset(test):
    test("unset A; echo $A", setup="export A=a")

@suite
def suite_pwd(test):
    test("pwd")
    test("pwd", setup="cd ..")
    test("pwd", setup="cd ../..")
    test("pwd", setup="cd ../../..")
    test("pwd", setup="cd /")
    test("pwd", setup="cd $HOME")

@suite
def suite_env(test):
    test("env")
    test("env", setup="export A=a")
    test("env", setup="export A=a B=b C=c")

@suite
def suite_exit(test):
    test("exit")
    test("exit 1")
    test("exit 2")
    test("exit 3")