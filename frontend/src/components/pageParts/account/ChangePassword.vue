<script setup>
import { reactive } from 'vue';
import Form from '@/components/form/Form.vue';
import Fieldset from '@/components/form/Fieldset.vue';
import Email from '@/components/form/fields/Email.vue';
import NewPassword from '@/components/form/fields/NewPassword.vue';
import Password from '@/components/form/fields/Password.vue';
import { validateMatch } from '@/utils/validation';


const errs = reactive({
    form: '',
    newPassword: { msg: '', invalid: false },
});

const models = reactive({
    currentPassword: '',
    newPassword: '',
    confirmPassword: ''
});

const checkPasswordsMatch = () => {
    validateMatch(models.newPassword, models.confirmPassword, errs.newPassword, 'Passwords do not match')
}

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
        <Password 
            placeholder="Current Password" 
            v-model="models.currentPassword"
        ></Password>
    </Fieldset>
    <Fieldset>
        <NewPassword 
            v-model="models.newPassword" 
            @focusout="checkPasswordsMatch"
            placeholder="New Password"
        ></NewPassword>
        <Password 
            v-model="models.confirmPassword" 
            @focusout="checkPasswordsMatch"
            :err="errs.newPassword"
            placeholder="Confirm Password"
        ></Password>
    </Fieldset>
</Form>    
</template>