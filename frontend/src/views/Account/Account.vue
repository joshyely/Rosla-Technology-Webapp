<script setup>
import { ref, reactive } from 'vue';
import Sidebar from '@/components/Sidebar.vue';
import Form from '@/components/form/Form.vue';
import Fieldset from '@/components/form/Fieldset.vue';
import Alpha from '@/components/form/fields/Alpha.vue';
import Date from '@/components/form/fields/Date.vue';
import Submit from '@/components/form/Submit.vue';
import DateWithSelects from '@/components/form/fields/DateWithSelects.vue';

const models = reactive({
    firstName: 'John',
    lastName: 'Doe',
    dob: ''
})

const sidebarRoutes = [
  {
    to: '/account/profile',
    display: 'Profile'
  },
  {
    to: '/account/security',
    display: 'Security'
  },
]

</script>

<template>
<section class="full">
<div class="flex">
    <Sidebar
      :routes="sidebarRoutes"
    >
        <template #top>
            <span id="sidebar-heading">Account Settings</span>
            <br>
        </template>
    </Sidebar>
    <div class="content">
        <RouterView></RouterView>
    </div>
</div>  
</section>
  

  
</template>

<style scoped lang="scss">
#sidebar-heading{
    font-size: 1.5rem;
    font-weight: 500;
    margin-bottom: 20px;
}
.content {
  flex: 3;
  padding: 40px;

  h1 {
    margin-bottom: 30px;
  }
  .submit-container{
    justify-content: flex-start;
    padding: 5% 1%;
  }
}
</style>