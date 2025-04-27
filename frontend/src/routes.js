import { createMemoryHistory, createRouter, createWebHistory } from 'vue-router'

import Home from './views/Home.vue'
import About from './views/About.vue'
import Contact from './views/Contact.vue'
import Login from './views/Login.vue'
import Register from './views/Register.vue'
import Products from './views/Products/Products.vue'
import ProductInfo from './views/Products/ProductInfo.vue'
import Account from './views/Account/Account.vue'
import Profile from './views/Account/Profile.vue'
import Security from './views/Account/Security.vue'

const routes = [
    { path: '/', component: Home, name: 'Home' },
    { path: '/about', component: About, name: 'About' },
    { path: '/contact', component: Contact, name: 'Contact' },
    { path: '/login', component: Login, name: 'Login' },
    { path: '/register', component: Register, name: 'Register' },
    { path: '/profile', component: Profile, name: 'Profile' },
    { 
        path: '/account',
        component: Account,
        name: 'Account',
        children: [
            {
                path: 'profile',
                component: Profile,
                name: 'Profile'
            },
            {
                path: 'security',
                component: Security,
                name: 'Account Security'
            },
        ]
    },
    { 
        path: '/products',
        component: Products, 
        name: 'Products' 
    },
    {
        path: '/products/:id',
        component: ProductInfo,
        name: 'Product Info'
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;