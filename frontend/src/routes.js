import { createMemoryHistory, createRouter, createWebHistory } from 'vue-router'
import { loggedIn } from './utils/auth'


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
import Appointments from './views/Account/Appointments.vue'
import AppointmentAbout from './views/Appointments/AppointmentAbout.vue'
import AppointmentBook from './views/Appointments/AppointmentBook.vue'


const devMode = true;
const checks = {
    isLoggedIn: (to, from) => {
        if (!loggedIn.value && !devMode){
            return { name: 'Login' }
        }
    },
}

const routes = [
    { path: '/', component: Home, name: 'Home' },
    { path: '/about', component: About, name: 'About' },
    { path: '/contact', component: Contact, name: 'Contact' },
    { path: '/login', component: Login, name: 'Login' },
    { path: '/register', component: Register, name: 'Register' },
    { 
        path: '/account',
        component: Account,
        name: 'Account Dashboard',
        beforeEnter: checks.isLoggedIn,
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
            {
                path: 'appointments',
                component: Appointments,
                name: 'User Appointments'
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
    },
    {
        path: '/appointments',
        component: AppointmentAbout,
        name: 'Appointments About'
    },
    {
        path: '/appointments/book',
        component: AppointmentBook,
        name: 'Appointments Book'
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;