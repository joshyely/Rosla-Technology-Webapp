<template>
    <div class="logo">
        <svg xmlns="http://www.w3.org/2000/svg">
            <image href="../assets/logo.png" />
        </svg>
        <span class="noto-sans-medium">
            Rosla Technology
        </span>
    </div>
</template>

<style scoped lang="scss">
.logo{
    display:flex;
    align-items: center;
    gap: 1rem;
    font-size: 1.2rem;
    svg{
        --logo-size: 50px;
        display:block;
        height: var(--logo-size);
        width: var(--logo-size);
        padding: 0;  
        image{
            height: 100%;
            width: 100%;
        }
    }
    span{
        color:var(--color-primary-1);
    }
}
    
    
</style>