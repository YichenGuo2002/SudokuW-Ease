<template>
    
    <div id="user-panel" class = "pl-48 h-16 bg-white text-black fixed items-center w-full flex flex-row-reverse p-2 border-b border-black">
        
        <button class = "h-8 w-8" id = "btn-close">
            <svg version="1.0" xmlns="http://www.w3.org/2000/svg"
            width="24px" height="24px" viewBox="0 0 24px 24px"
            preserveAspectRatio="xMidYMid meet">
            <metadata>
            Created by potrace 1.16, written by Peter Selinger 2001-2019
            </metadata>
            <g transform="translate(0.000000,24.000000) scale(0.009600,-0.009600)"
            fill="#000000" stroke="none">
            <path d="M345 2150 l-39 -40 429 -430 430 -430 -430 -430 -430 -430 43 -42 42
            -43 430 430 430 430 430 -430 430 -430 42 43 43 42 -430 430 -430 430 430 430
            430 430 -43 42 -42 43 -430 -430 -430 -430 -428 428 c-235 235 -430 427 -433
            427 -2 0 -23 -18 -44 -40z"/>
            </g>
            </svg>
        </button>
        <button class = "h-8 w-8 ml-2" id = "btn-minimize">
            <svg xmlns="http://www.w3.org/2000/svg" version="1.0" width="24px" height="24px" viewBox="0 0 24px 24px" preserveAspectRatio="xMidYMid meet">
            <metadata>
            Created by potrace 1.16, written by Peter Selinger 2001-2019
            </metadata>
            <g transform="translate(0.000000,24.000000) scale(0.024000,-0.024000)" fill="#000000" stroke="none">
            <path d="M762 797 l-162 -162 0 93 c0 85 -1 92 -20 92 -19 0 -20 -7 -20 -130 l0 -130 130 0 c123 0 130 1 130 20 0 19 -7 20 -92 20 l-93 0 163 163 c155 156 162 164 145 180 -18 15 -27 8 -181 -146z"/>
            <path d="M180 420 c0 -19 7 -20 92 -20 l93 0 -163 -163 c-154 -154 -161 -163 -145 -180 17 -16 26 -9 180 145 l163 163 0 -93 c0 -85 1 -92 20 -92 19 0 20 7 20 130 l0 130 -130 0 c-123 0 -130 -1 -130 -20z"/>
            </g>
            </svg>
        </button>

        <div id="user-dropdown" class = "relative flex-initial ml-4">
            <button @click = "isOpen = !isOpen" class = "h-8 w-8">
                    <svg version="1.0"
                    width="24px" height="24px" viewBox="0 0 24px 24px"
                    preserveAspectRatio="xMidYMid meet">
                    <metadata>
                    Created by potrace 1.16, written by Peter Selinger 2001-2019
                    </metadata>
                    <g transform="translate(0.000000,24.000000) scale(0.009600,-0.009600)"
                    fill="#000000" stroke="none">
                    <path d="M0 2000 l0 -50 1250 0 1250 0 0 50 0 50 -1250 0 -1250 0 0 -50z"/>
                    <path d="M0 1250 l0 -50 1250 0 1250 0 0 50 0 50 -1250 0 -1250 0 0 -50z"/>
                    <path d="M0 500 l0 -50 1250 0 1250 0 0 50 0 50 -1250 0 -1250 0 0 -50z"/>
                    </g>
                    </svg>
            </button>
            <button v-if="isOpen" @click = "isOpen = false" tabindex = "-1" class = "fixed pin h-full w-full cursor-default"></button>
            <div v-if="isOpen" class="absolute pin-r mt-2 bg-grey-lighter rounded-lg py-2 w-32 shadow-lg">
                    <router-link :to="'/home'" class="block px-4 py-2 text-black no-underline hover:bg-grey">Sign In</router-link>
                    <router-link :to="'/home'" class="block px-4 py-2 text-black no-underline hover:bg-grey">Sign Out</router-link>
            </div>
        </div>

        <div id="user-icon" class = "block h-8 w-8 rounded-full overflow-hidden border border-black">
            <img src="../assets/icon_user.png" />
        </div>

    </div>

    <nav id="nav" class="w-48 bg-white text-black fixed min-h-screen pt-2 pb-2 flex flex-col justify-between border-r border-black">
        
        <div class = "sidebar-icons flex flex-col items-center">
            
            <div class = "h-12">
                <img src ="../assets/sudoku_logo.png" class = "h-12"/>
            </div>

            <button class="sidebar-icon flex-initial flex justify-around items-center px-4 py-2 text-black cursor-pointer bg-white mt-4 mb-4 rounded-lg w-close hover:bg-grey-lighter">
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
                <router-link :to="'/'" class="text-black no-underline">&nbsp;&nbsp;Solve Sudoku&nbsp;&nbsp;</router-link>
            </button>
            <button class="sidebar-icon flex-initial flex justify-around items-center px-4 py-2 text-black cursor-pointer bg-white mb-4 rounded-lg w-close hover:bg-grey-lighter">
                <svg version="1.0" xmlns="http://www.w3.org/2000/svg"
                width="24px" height="24px" viewBox="0 0 24px 24px"
                preserveAspectRatio="xMidYMid meet">
                <metadata>
                Created by potrace 1.16, written by Peter Selinger 2001-2019
                </metadata>
                <g transform="translate(0.000000,24.000000) scale(0.009600,-0.009600)"
                fill="#000000" stroke="none">
                <path d="M212 2288 c-17 -17 -17 -2059 0 -2076 17 -17 2059 -17 2076 0 17 17
                17 2059 0 2076 -17 17 -2059 17 -2076 0z m1988 -1038 l0 -950 -950 0 -950 0 0
                950 0 950 950 0 950 0 0 -950z"/>
                <path d="M535 2031 c-50 -22 -109 -86 -125 -136 -8 -23 -11 -68 -8 -114 9
                -141 80 -234 286 -373 l112 -76 113 76 c205 139 276 232 285 373 5 93 -8 138
                -57 192 -48 54 -101 77 -179 77 -62 0 -107 -15 -144 -48 -16 -14 -20 -14 -35
                0 -58 51 -172 64 -248 29z m190 -122 c19 -17 43 -44 52 -60 10 -16 20 -29 23
                -29 3 0 18 20 34 44 38 56 72 76 131 76 42 0 52 -5 86 -39 35 -35 39 -44 39
                -90 0 -28 -6 -67 -14 -86 -21 -50 -98 -128 -193 -197 l-83 -59 -83 59 c-95 69
                -172 147 -193 197 -8 19 -14 58 -14 86 0 46 4 55 39 90 35 35 44 39 89 39 43
                0 57 -5 87 -31z"/>
                <path d="M1300 2000 l0 -50 400 0 400 0 0 50 0 50 -400 0 -400 0 0 -50z"/>
                <path d="M1300 1700 l0 -50 400 0 400 0 0 50 0 50 -400 0 -400 0 0 -50z"/>
                <path d="M1300 1400 l0 -50 400 0 400 0 0 50 0 50 -400 0 -400 0 0 -50z"/>
                <path d="M400 1100 l0 -50 400 0 400 0 0 50 0 50 -400 0 -400 0 0 -50z"/>
                <path d="M1300 1100 l0 -50 400 0 400 0 0 50 0 50 -400 0 -400 0 0 -50z"/>
                <path d="M400 800 l0 -50 400 0 400 0 0 50 0 50 -400 0 -400 0 0 -50z"/>
                <path d="M1300 800 l0 -50 400 0 400 0 0 50 0 50 -400 0 -400 0 0 -50z"/>
                <path d="M400 500 l0 -50 400 0 400 0 0 50 0 50 -400 0 -400 0 0 -50z"/>
                <path d="M1300 500 l0 -50 400 0 400 0 0 50 0 50 -400 0 -400 0 0 -50z"/>
                </g>
                </svg>
                <router-link :to="'/find'" class="text-black no-underline">&nbsp;&nbsp;Find Sudoku&nbsp;&nbsp;&nbsp;</router-link>
            </button>
            <button class="sidebar-icon flex-initial flex justify-around items-center px-4 py-2 text-black cursor-pointer bg-white mb-4 rounded-lg w-close hover:bg-grey-lighter">
                <svg version="1.0" xmlns="http://www.w3.org/2000/svg"
                width="24px" height="24px" viewBox="0 0 24px 24px"
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
                <router-link :to="'/upload'" class="text-black no-underline">&nbsp;&nbsp;Upload Puzzle&nbsp;</router-link>
            </button>
            <button class="sidebar-icon flex-initial flex justify-around items-center px-4 py-2 text-black cursor-pointer bg-white mb-4 rounded-lg w-close hover:bg-grey-lighter">
                <svg version="1.0" xmlns="http://www.w3.org/2000/svg"
                width="24px" height="24px" viewBox="0 0 24px 24px"
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
                <router-link :to="'/about'" class="text-black no-underline">&nbsp;&nbsp;About Creator</router-link>
            </button>

        </div>
        
        <div id = "copyright" class = "flex flex-col pl-2">
            
            <p class = "pt-1">About/Press/Copyright</p>
            <p class = "pt-1">Contact Us/Creators</p>
            <h6 class = "pt-1">
                <a href = "" class = "text-grey no-underline">©2023 Yichen Guo LLC</a>
            </h6>
        
        </div>
    
    </nav>

</template>

<script>

export default{
    data(){
        return{
            isOpen:false
        }
    },
}
</script>