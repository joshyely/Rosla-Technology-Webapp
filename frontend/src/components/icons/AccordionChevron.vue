<template>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" fill="#e8eaed">
        <path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/>
    </svg>
</template>

<style scoped lang="scss">
svg {
    fill: var(--color-text);
    display:flex;
    align-items: center;
    justify-content: center;
    transition: all .5s ease-in-out;
    --size: 2.2em;
    width: var(--size);
    height: var(--size);
    &.active{
        transform: rotate(90deg);
    }
    path{
        font-weight: 100;
    }
}
</style>