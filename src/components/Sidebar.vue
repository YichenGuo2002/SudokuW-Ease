<template>
    <div id="nav" class="w-64 bg-white text-black fixed min-h-screen pt-8">
        <div class = "sidebar-icons">
            <div class="sidebar-icon flex items-center px-4 py-2 text-black cursor-pointer bg-white hover:bg-grey-lighter">
                <svg version="1.0" xmlns="http://www.w3.org/2000/svg"
                width="24px" height="24px" viewBox="0 0 24px 24px"
                preserveAspectRatio="xMidYMid meet">
                <metadata>
                Created by potrace 1.16, written by Peter Selinger 2001-2019
                </metadata>
                <g transform="translate(0.000000,23.000000) scale(0.009600,-0.009200)"
                fill="#000000" stroke="none">
                <path d="M2035 2371 c-27 -16 -61 -41 -75 -55 l-24 -27 177 -177 176 -176 31
                29 c17 16 42 53 56 82 23 46 26 63 22 127 -3 64 -8 81 -33 118 -17 23 -50 56
                -74 73 -38 27 -52 30 -124 33 -75 3 -86 0 -132 -27z"/>
                <path d="M1022 1377 l-822 -822 -50 -187 c-52 -195 -58 -236 -38 -256 20 -20
                61 -14 256 38 l187 50 822 822 c868 868 851 849 807 892 -8 9 -25 16 -37 16
                -16 0 -256 -234 -834 -812 l-813 -813 -97 98 -98 97 813 813 c479 479 812 819
                812 830 0 36 -19 57 -53 57 -29 0 -105 -73 -855 -823z"/>
                </g>
                </svg>
                <div>&nbsp;&nbsp;Solve</div>
            </div>
            <div class="sidebar-icon flex items-center px-4 py-2 text-black cursor-pointer bg-white hover:bg-grey-lighter">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Layer_1" x="0px" y="0px" width="24px" height="24px" viewBox="0 0 250 250" enable-background="new 0 0 250 250" xml:space="preserve">  <image id="image0" width="250" height="250" x="0" y="0" href="data:image/png;base64,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"/></svg>
                <div>&nbsp;&nbsp;Discover</div>
            </div>
            <div class="sidebar-icon flex items-center px-4 py-2 text-black cursor-pointer bg-white hover:bg-grey-lighter">
                <svg version="1.0" xmlns="http://www.w3.org/2000/svg"
                width="24px" height="24px" viewBox="0 0 24.000000 24.000000"
                preserveAspectRatio="xMidYMid meet">
                <metadata>
                Created by potrace 1.16, written by Peter Selinger 2001-2019
                </metadata>
                <g transform="translate(0.000000,24.000000) scale(0.009600,-0.009600)"
                fill="#000000" stroke="none">
                <path d="M0 1250 l0 -1050 1250 0 1250 0 0 1050 0 1050 -1250 0 -1250 0 0
                -1050z m2400 0 l0 -950 -1150 0 -1150 0 0 950 0 950 1150 0 1150 0 0 -950z"/>
                <path d="M198 1528 c-2 -315 -2 -698 0 -850 l3 -278 1049 0 1049 0 3 128 c2
                70 2 452 0 850 l-2 722 -1050 0 -1050 0 -2 -572z m2002 -135 l0 -607 -233 232
                c-211 210 -236 232 -266 232 -30 0 -48 -14 -143 -107 l-108 -107 -24 24 c-13
                14 -128 140 -256 280 -128 140 -241 258 -252 262 -11 5 -29 3 -43 -5 -12 -6
                -130 -111 -261 -233 -132 -121 -256 -235 -276 -253 l-38 -33 0 461 0 461 950
                0 950 0 0 -607z m-1056 -193 l225 -245 -61 -62 c-48 -49 -61 -68 -61 -93 0
                -39 14 -53 54 -53 28 0 46 14 128 99 53 55 136 137 184 184 l88 84 249 -249
                250 -250 0 -57 0 -58 -950 0 -950 0 0 209 0 209 298 275 c227 210 300 272 309
                264 6 -7 113 -122 237 -257z"/>
                <path d="M1666 1731 c-46 -31 -66 -69 -66 -131 0 -62 20 -100 66 -131 20 -13
                47 -19 84 -19 62 0 100 20 131 66 26 39 26 129 0 168 -31 46 -69 66 -131 66
                -37 0 -64 -6 -84 -19z"/>
                </g>
                </svg>
                <div>&nbsp;&nbsp;Upload</div>
            </div>
            <div class="sidebar-icon flex items-center px-4 py-2 text-black cursor-pointer bg-white hover:bg-grey-lighter">
                <svg version="1.0" xmlns="http://www.w3.org/2000/svg"
                width="24px" height="24px" viewBox="0 0 24.000000 24.000000"
                preserveAspectRatio="xMidYMid meet">
                <metadata>
                Created by potrace 1.16, written by Peter Selinger 2001-2019
                </metadata>
                <g transform="translate(0.000000,24.000000) scale(0.009600,-0.009600)"
                fill="#000000" stroke="none">
                <path d="M1005 2435 c-193 -35 -416 -130 -560 -237 -204 -152 -354 -368 -417
                -598 -20 -75 -23 -107 -22 -265 0 -166 2 -187 27 -268 51 -165 143 -321 266
                -450 l55 -58 -21 -42 c-33 -69 -97 -142 -194 -222 -111 -91 -133 -118 -133
                -161 0 -44 17 -62 82 -80 43 -13 82 -15 171 -11 168 7 375 64 658 180 l62 25
                98 -15 c175 -27 408 -6 596 54 318 100 596 332 726 606 155 327 129 703 -71
                1009 -165 253 -426 432 -752 515 -88 22 -127 26 -296 29 -141 2 -217 -1 -275
                -11z m375 -100 c173 -11 382 -83 541 -186 216 -141 363 -335 435 -574 25 -81
                27 -105 27 -240 0 -135 -2 -159 -27 -239 -124 -410 -485 -694 -961 -757 -98
                -13 -284 -7 -375 11 -54 11 -58 10 -180 -38 -309 -123 -582 -186 -664 -153
                -16 6 -9 15 47 59 128 102 214 216 247 329 l13 41 -86 86 c-132 132 -217 275
                -265 448 -24 89 -24 347 0 436 106 383 435 673 863 762 65 13 234 28 275 24
                14 -2 63 -6 110 -9z"/>
                <path d="M1170 1775 l0 -85 80 0 80 0 0 85 0 85 -80 0 -80 0 0 -85z"/>
                <path d="M1175 1487 c-3 -6 -4 -167 -3 -357 l3 -345 78 -3 77 -3 0 361 0 360
                -75 0 c-52 0 -77 -4 -80 -13z"/>
                </g>
                </svg>
                <div>&nbsp;&nbsp;About</div>
            </div>
        </div>
    </div>
</template>