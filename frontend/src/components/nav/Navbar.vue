<script setup>
import Logo from '../Logo.vue';
import MenuIcon from '../icons/mobile/Menu.vue'
import CloseIcon from '../icons/mobile/Close.vue'
import MainNav from './lists/Main.vue'
import AccountNav from './lists/Account.vue'
import { mobile } from '@/utils/responsive.js';


import { ref, watch } from 'vue';
import { useRoute } from 'vue-router';


const route = useRoute();
const currentPage = ref();

const menuOpen = ref(false);

watch(
    () => mobile,
    (mobile) => {
        console.log('running watcher')
        if(!mobile){
            menuOpen.value = false;
        }
    }
);

const menuToggle = () => menuOpen.value = menuOpen.value==true ? false : true;

watch(
  () => route.fullPath,
  (fullPath) => {
    menuOpen.value = false;
    currentPage.value = fullPath;
  }
);
</script>

<template>

<div id="mobile" class="navbar-wrapper" v-if="mobile">
    <div class="nav-container">
        <RouterLink class="logo-link" to="/"><Logo /></RouterLink>
        
        <MenuIcon @click="menuToggle" v-if="!menuOpen"/>
        <CloseIcon @click="menuToggle" v-else/>
        
        
    </div>
    <transition name="menu">
        <div id="menu" v-show="menuOpen">
            <AccountNav />
            <MainNav />
        </div>
    </transition>
    
</div>
<div id="desktop" class="navbar-wrapper" v-else>
    <div class="nav-container">
        <RouterLink class="logo-link" to="/"><Logo /></RouterLink>
        <nav>
           <MainNav />
           <AccountNav />
        </nav>
    </div>
</div>
</template>


<style lang="scss">
.logo-link{ 
    text-decoration: none;
}

.navbar-wrapper {
    background-color: var(--color-background);
    border-bottom: solid 1px var(--color-border);
    display:flex;
    justify-content: center;
}

.nav-container,
nav
{
    display:flex;
}
.nav-container{
    width: 95rem;
    max-width:100%;
    gap: 10%;
    align-items: center;
}
.nav-list{
    list-style:none;
    display:flex;
    align-content: center;
}
.nav-item{
    align-content: center;
    a{
        font-size: 1.23rem;
        text-decoration: none;
        font-weight:500;
        display: block;
    }
}

#desktop {
    padding:0 3%;
    --nav-height: 80px;
    height: var(--nav-height);
    nav {
        height: 100%;
        flex-grow: 1;
    }
    .nav-list {
        height: 100%;
        padding: 0;
        gap: 30px;
        font-size:1rem;
    }
    #account-nav {
        justify-content: end;
        flex-grow: 1;
    }
    .nav-item {
        height: 100%;
        width: fit-content;
        a {
            width: 100%;
            height: 100%;
            color:var(--color-text);
            margin: 0 1%;
            padding: 0 10px;
            transition: color .1s ease-in-out;
            align-content: center;
        }
        a:hover{
            color: var(--color-primary-2);
        }
        a.router-link-active{
            border-bottom: 3px solid var(--color-primary-2);;
        }
    }
}
#mobile{
    padding: 0 1%;
    --nav-height: 70px;
    height: var(--nav-height);
    .logo{
        --logo-size: var(--nav-height);
    }
    .nav-container{
        justify-content: space-between;
    }
    #menu {
        padding: 2% 0;
        position: absolute;
        inset: 0;
        inset-block-start: calc(var(--nav-height));
        background-color: var(--color-background);
        border-left: 1px solid var(--color-border);
        z-index: 2147483647;
    }
    .menu-enter-active{
        animation: slide-in .5s;
    }
    .menu-leave-active{
        animation: slide-out .5s;
    }
    .nav-list{
        padding:0;
        flex-direction: column;
        font-size:1.2rem;
    }
    .nav-item{
        width:100%;
    }
    #main-nav{
        margin: 20px 0;
        a {
            padding: 10px 30px 10px 30px;
            color: var(--color-text);
            display: inline-flex;
        }
        a.router-link-active{
            border-left: 3px solid var(--theme-color-2);
            color: var(--theme-color-2);
        }
    }
    #account-nav {
        margin: 20px 8%;
        gap: 15px;
        .nav-item {
            a{
                display:inline-flex;
                inline-size: 100%;
                align-items: center;
                justify-content: center;
                block-size: 50px;
                border-radius: 100px;
                border: 1px solid var(--color-primary-2);
                color: var(--color-primary-2);
            }
        }
        .nav-item:first-child a {
            background-color: var(--color-primary-2);
            color: #ffffffff;
        }
    }

}
</style>