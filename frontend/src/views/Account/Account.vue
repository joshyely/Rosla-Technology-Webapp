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



const accountRoutes = [
  {
    to: '/account/energy-and-devices',
    display: 'Energy and Devices'
  },
  {
    to: '/account/appointments',
    display: 'Appointments'
  },
]

const settingsRoutes = [
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
<section class="mid">
<div class="flex">
  <aside>
    <Sidebar
      :routes="accountRoutes"
      heading="Account"
    >
    </Sidebar>
    <Sidebar
      :routes="settingsRoutes"
      heading="Settings"
    >
    </Sidebar>

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