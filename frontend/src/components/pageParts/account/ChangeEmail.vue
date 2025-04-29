<script setup>
import { reactive } from 'vue';
import Form from '@/components/form/Form.vue';
import Fieldset from '@/components/form/Fieldset.vue';
import Email from '@/components/form/fields/Email.vue';
import Password from '@/components/form/fields/Password.vue';

const props = defineProps({
    currentEmail:{
        type: String,
        default: ''
    },
})


const errs = reactive({
    form: ''
});

const models = reactive({
    email: props.currentEmail,
    password: ''
});

const submit = async () => {
    console.log('submitting..')
};

const submitInvalid = () => {
    console.log('submission invalid.')
};

</script>

<template>
<Form
    submit-value="Change"
    @submit="submit" 
    @invalid-submit="submitInvalid"
    :err-msg="errs.form"
>
    <Fieldset>
        <Email v-model="models.email"></Email>
        <Password v-model="models.password"></Password>
    </Fieldset>
</Form>    
</template>