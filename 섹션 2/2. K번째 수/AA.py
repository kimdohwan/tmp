'''6 2 5 3
5, 2, 7, 3, 8, 9
15 3 10 3
4 15 8 16 6 6 17 3 10 11 18 7 14 7 15 '''

if __name__ == '__main__':
    s, e, k = 200,400,176

    l = [int(i) for i in '169 653 252 164 765 527 115 784 18 623 270 623 868 676 121 999 459 277 49 702 792 11 307 85 316 925 40 871 844 422 685 288 299 332 376 329 142 218 549 571 365 841 762 970 912 99 215 621 561 848 307 651 193 964 323 167 429 368 675 111 394 919 850 489 734 453 577 135 890 515 756 550 981 806 805 969 74 633 117 531 181 392 221 365 609 687 492 860 334 777 985 958 601 469 179 935 461 630 431 743 953 243 778 414 969 630 255 172 49 848 779 762 39 709 352 748 913 916 335 259 559 994 425 862 778 631 184 49 469 81 249 105 667 512 613 270 978 722 472 922 230 295 737 57 400 663 300 265 440 67 492 172 177 298 261 828 628 181 496 591 296 317 152 659 601 115 542 324 966 392 552 123 936 974 719 801 839 487 96 636 223 540 955 49 35 497 955 123 320 111 101 266 790 218 156 176 482 524 268 728 511 713 862 400 647 565 268 481 12 939 350 604 452 720 835 207 829 230 243 265 413 325 637 186 877 263 621 374 966 731 81 275 893 430 739 705 539 36 49 530 584 148 100 706 249 133 134 145 800 507 295 334 699 15 561 334 263 230 803 70 406 641 155 397 6 813 488 941 717 731 614 251 298 611 891 965 894 828 202 997 194 399 854 131 594 517 753 103 963 262 533 567 545 140 19 933 60 968 218 109 444 515 99 126 211 582 3 966 665 302 976 539 646 578 327 552 979 920 141 756 74 568 308 425 591 334 89 596 271 133 708 928 448 930 64 272 921 991 987 549 932 497 584 188 793 549 699 676 661 990 844 502 930 954 200 766 681 773 365 41 701 310 541 679 386 737 116 915 574 525 597 577 295 575 201 304 53 878 850 448 377 248 32 189 253 293 945 964 110 459 734 29 960 170 268 898 537 681 56 991 393 7 623 939 48 143 661 582 225 502 468 531 253 127 63 768 771 593 319 419 870 911 206 727 199 144 410 144 950 184 964 307 379 327 58 778 113 560 146 431 581 421 976 614 419 809 578 135 523 622 66 788 882 25 907 480 115 802 759 769 759 656 112 312 611 204 398 567 409 868 961 362 778 4 768 176 627 160 409 827 93 821 201 54 225 216 318 504 483 775 611 615 102 951 356 630 713 726 643 729'.split(' ')]

    a = l[s - 1:e - 1]
    a.sort()
    print(a[k - 1])
