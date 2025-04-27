<script setup>
import { loggedIn, logout } from '@/utils/auth';
import Button from '@/components/buttons/Button.vue';
import ButtonPrimary from '@/components/buttons/ButtonPrimary.vue';
import ButtonSecondary from '@/components/buttons/ButtonSecondary.vue';
</script>

<template>
<ul id="account-nav" class="nav-list" v-if="!loggedIn">
    <li class="nav-item">
        <RouterLink to="/login">Login</RouterLink>
    </li>
    <li class="nav-item">
        <RouterLink to="/register">Register</RouterLink>
    </li>
</ul>
<ul id="account-nav" class="nav-list" v-else>
    <li class="nav-item">
        <RouterLink to="/account">Account</RouterLink>
    </li>
    <li class="nav-item">
        <a @click="logout" class="pointer-hover">Logout</a>
    </li>
</ul>
</template>