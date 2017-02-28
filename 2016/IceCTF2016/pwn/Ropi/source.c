function main {
    ezy();
    puts("addio!");
    return 0x0;
}

function ezy {
    puts("Benvenuti al convegno RetOri Pro!\nVuole lasciare un messaggio?");
    eax = *stdout@@GLIBC_2.0;
    fflush(eax);
    eax = read(0x0, var_28, 0x40);
    return eax;
}

function ret {
    if (arg0 != 0xbadbeeef) {
            puts("chiave sbagliata! :(");
            exit(0x1);
    }
    else {
            *fd = open("./flag.txt", 0x0);
            puts("[+] aperto");
            eax = *stdout@@GLIBC_2.0;
            fflush(eax);
    }
    return;
}

function ori {
    if ((arg0 != 0xabcdefff) && (arg1 != 0x78563412)) {
            puts("chiave sbagliata! :((");
            exit(0x1);
    }
    else {
            eax = *fd;
            read(eax, 0x804a080, 0x80);
            puts("[+] leggi");
            eax = *stdout@@GLIBC_2.0;
            fflush(eax);
    }
    return;
}

function pro {
    puts("[+] stampare");
    printf(0x80487b7, 0x804a080);
    eax = *stdout@@GLIBC_2.0;
    eax = fflush(eax);
    return eax;
}
