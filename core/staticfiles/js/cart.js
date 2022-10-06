const productContainer = document.querySelector('.product-container');
const quantity = document.querySelector('.order-container');

const updateUserOrder = async function (productId, action) {
  url = '/update_item/';
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({ productId: productId, action: action }),
  });
  const data = await response.json();
  location.reload();
};

if (quantity) {
  quantity.addEventListener('click', function (e) {
    const btn = e.target.closest('.update-cart');
    if (!btn) return;
    const { productId, action } = btn.dataset;
    if (user === 'AnonymousUser') console.log('Not logged in');
    else {
      updateUserOrder(productId, action);
    }
  });
}


if (productContainer) {
  productContainer.addEventListener('click', function (e) {
    const btn = e.target.closest('.update-cart');
    console.log(btn);
    if (!btn) return;
    const { productId, action } = btn.dataset;
    console.log(productId, action);

    if (user === 'AnonymousUser') console.log('Not logged in');
    else {
      updateUserOrder(productId, action);
    }
  });
}
