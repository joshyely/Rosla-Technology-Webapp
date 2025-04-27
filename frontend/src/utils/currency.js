export const formatPrice = (price) => {
    let asDecimal = price / 100
    return asDecimal.toLocaleString(
        'en-GB', 
        {
            style: 'currency',
            currency: 'GBP',
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        }
    );
};