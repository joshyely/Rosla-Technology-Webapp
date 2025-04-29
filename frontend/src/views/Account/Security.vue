<script setup>
import { reactive } from 'vue';
import Form from '@/components/form/Form.vue';
import Fieldset from '@/components/form/Fieldset.vue';
import Email from '@/components/form/fields/Email.vue';
import Alpha from '@/components/form/fields/Alpha.vue';
import Date from '@/components/form/fields/Date.vue';
import Password from '@/components/form/fields/Password.vue';
import NewPassword from '@/components/form/fields/NewPassword.vue';
import Submit from '@/components/form/Submit.vue';
import Accordion from '@/components/Accordion.vue';

import ChangeEmail from '@/components/pageParts/account/ChangeEmail.vue';
import ChangePassword from '@/components/pageParts/account/ChangePassword.vue';


const accordionHeadingSize = '1rem';

const data = {
    email: 'johndoe@example.com',
    phone: '0123456789'
}
</script>

<template>
<h1>Security</h1>
<br>
<div class="container">
    <Accordion 
        heading="Change Email"
        :heading-size="accordionHeadingSize"
    >
        <ChangeEmail :current-email="data.email"></ChangeEmail>
    </Accordion>
    <Accordion
        heading="Change Password"
        :heading-size="accordionHeadingSize"
    >
        <ChangePassword></ChangePassword>
    </Accordion>
</div>
</template>