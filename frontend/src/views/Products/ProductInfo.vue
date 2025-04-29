<script setup>
import { formatPrice } from '@/utils/currency';
import ButtonPrimary from '@/components/buttons/ButtonPrimary.vue';
import ProductCard from '@/components/cards/ProductCard.vue';
import placeholders from '@/utils/placeholders';
const product = {
    id: 1,
    name: 'Product',
    description: placeholders.paragraph,
    model: 'ABC1234DE56',
    imageUrl: '/src/assets/blankImage.png',
    stock: 0,
    price: 1,
    discount: {
        amount: 0,
        percent: 0
    }
}
const similarProducts = [
    {
        id: 1,
        name: 'Product',
        description: 'No Description',
        model: 'ABC1234DE56',
        imageUrl: '/src/assets/blankImage.png',
        stock: 0,
        price: 1,
        discount: {
            amount: 0,
            percent: 0
        }
    },
    {
        id: 1,
        name: 'Product',
        description: 'No Description',
        model: 'ABC1234DE56',
        imageUrl: '/src/assets/blankImage.png',
        stock: 0,
        price: 1,
        discount: {
            amount: 0,
            percent: 0
        }
    },
    {
        id: 1,
        name: 'Product',
        description: 'No Description',
        model: 'ABC1234DE56',
        imageUrl: '/src/assets/blankImage.png',
        stock: 0,
        price: 1,
        discount: {
            amount: 0,
            percent: 0
        }
    },
]

</script>

<template>
<section class="full" id="product-basic">
    <div class="flex" style="gap:8%;">
        <div class="container flex-primary">
            <img :src="product.imageUrl" alt="img" width="100%">
        </div>
        <div class="container" id="product-info">
            <div id="top-info">
                <h1 style="font-size: 2.4rem;">{{ product.name }}</h1>
                <p id="product-model">{{ product.model }}</p>
            </div>
            <div id="purchase-info" class="container">
                <div class="container">
                    <div id="pricing">
                        <span id="price">{{ formatPrice(product.price) }}</span>
                    </div>
                    <div id="stock">
                        <span id="in-stock" v-if="product.stock >= 25">In Stock</span>
                        <span id="low-stock" v-else-if="product.stock > 0">Hurry! Only {{ product.stock }} left in Stock</span>
                        <span id="no-stock" v-else>Out of Stock</span>
                    </div>
                </div>
                <div id="purchase-buttons">
                    <ButtonPrimary :disabled="product.stock <= 0">Add to Cart</ButtonPrimary>
                </div> 
            </div>
        </div>
    </div>
</section>
<section class="full" id="product-more">
    <div class="flex">
        <div class="container flex-primary">
            <article>
                <h2>Description</h2>
                {{ product.description }}
            </article>
        </div>
        <div class="container flex-secondary">
            <aside>
                <h3>Similar Products</h3>
                <div id="similar-products">
                    <ProductCard v-for="product in similarProducts" :product="product"></ProductCard>
                </div>
            </aside>
        </div>
    </div>
</section>
</template>

<style scoped lang="scss">
#product-basic{
    min-height: 60vh;
    border-bottom: var(--border-heavy);
    #product-info{
        display: flex;
        flex-direction: column;
        justify-content: space-evenly;
        #purchase-info{
            #pricing{
                flex:.5;
                font-size: 1.3rem;
                #price{
                    font-weight: 600;
                }
            }
            #stock{
                width:fit-content;
                flex:auto;
                #in-stock{
                    color: var(--color-success);
                }
                #low-stock{
                    color: var(--color-warning);
                }
                #no-stock{
                    color: var(--color-error);
                }
            }
        }
    }
}
#product-more{
    .flex{
        min-height: inherit;
    }
    
    aside{
        min-height: inherit;
        display:flex;
        flex-direction: column;
        #similar-products{
            display: flex;
            padding: 5% 3%;
            flex: 1;
            gap: 3%;
            width: fit-content;
            overflow-x: scroll;
            
            .product-card{
                flex-grow: 1;
            }
        }
    }
}
</style>