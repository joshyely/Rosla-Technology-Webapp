<script setup>
import { reactive } from 'vue';
import Form from '@/components/form/Form.vue';
import Fieldset from '@/components/form/Fieldset.vue';
import Email from '@/components/form/fields/Email.vue';
import Alpha from '@/components/form/fields/Alpha.vue';
import Date from '@/components/form/fields/Date.vue';
import Submit from '@/components/form/Submit.vue';

const models = reactive({
    email: 'johndoe@example.com',
    phone: '0123456789'
});
</script>

<template>
<h1>Security</h1>
<div class="container">
    <div class="email-section">
        <p>Email: <span>{{ models.email }}</span></p>
    </div>
    <div class="phone-section">
        <p>Phone: <span>{{ models.phone }}</span></p>
    </div>
</div>
</template>