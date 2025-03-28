<template>
    <svg class="menu-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960">
        <path d="M164-278.62v-51.99h632v51.99H164ZM164-454v-52h632v52H164Zm0-175.39v-51.99h632v51.99H164Z"/>
        <circle class="sb-icon-hover" cx="50%" cy="-50%" r="50%"></circle>
    </svg>
</template>

<style scoped>
svg{
    height: 50px;
    width: 50px;
    fill: var(--color-mobile-btn);
}
circle{
    opacity: .15;
    fill: transparent;
    transition: fill .15s ease-in-out;
}
svg {
    width: 85px;
}
svg:hover {
    cursor:pointer;
}
svg:hover circle{
    fill:var(--color-mobile-hover-circle);
}
svg:active{
    transform:scale(95%);
}
</style>
