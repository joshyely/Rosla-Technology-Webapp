<script setup>
</script>

<template>
<section class="mid">
<div class="flex">
  <aside>
    <slot></slot>
  </aside>
    
  <div class="content">
      <RouterView></RouterView>
  </div>
</div>  
</section>
</template>

<style scoped lang="scss">
aside{
  flex: 1;
}

#sidebar-heading{
    font-size: 1.5rem;
    font-weight: 500;
    margin-bottom: 20px;
}
.content {
  flex: 3;
  padding: 30px 0;
  @media(min-width:1024px){
    padding: 40px;
  }

  h1 {
    margin-bottom: 30px;
  }
  .submit-container{
    justify-content: flex-start;
    padding: 5% 1%;
  }
}
</style>