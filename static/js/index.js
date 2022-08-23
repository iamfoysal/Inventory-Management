const message = document.querySelector('.message');

if (message) {
   setTimeout(() => {
     message.classList.add("message-hide");
   }, 5000);
}



document.querySelector(".jsFilter").addEventListener("click", function () {
    document.querySelector(".filter-menu").classList.toggle("active");
  });
  
  document.querySelector(".grid").addEventListener("click", function () {
    document.querySelector(".list").classList.remove("active");
    document.querySelector(".grid").classList.add("active");
    document.querySelector(".products-area-wrapper").classList.add("gridView");
    document
      .querySelector(".products-area-wrapper")
      .classList.remove("tableView");
  });
  
  document.querySelector(".list").addEventListener("click", function () {
    document.querySelector(".list").classList.add("active");
    document.querySelector(".grid").classList.remove("active");
    document.querySelector(".products-area-wrapper").classList.remove("gridView");
    document.querySelector(".products-area-wrapper").classList.add("tableView");
  });
  
  


//index view from api

let productContainer = document.querySelector(".product-wrapper")
productContainer.innerHTML = ''

  function buildProduct(){

    let url = 'http://127.0.0.1:8000/api/'
    fetch(url)
    .then((resp) => resp.json())
    .then(function(data){
      console.log(data)

      let product = data
      for (let i in product){
        let products = `
        <div class="products-row" id='productId-${i}'>
        <button class="cell-more-button">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="18"
            height="18"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            class="feather feather-more-vertical"
          >
            <circle cx="12" cy="12" r="1" />
            <circle cx="12" cy="5" r="1" />
            <circle cx="12" cy="19" r="1" />
          </svg>
        </button>
        <div class="product-cell image">
          <img
          src="${product[i].image}"
            alt="product"
          />
          <span>${ product[i].title }</span>
        </div>
        <div class="product-cell category">
          <span class="cell-label">Category:</span>${ product[i].category}
        </div>

        <div class="product-cell stock">
          <span class="cell-label">Stock:</span>${ product[i].stock }
        </div>

        <div class="product-cell price">
          <span class="cell-label">Price:</span>$ ${ product[i].price }
        </div>

        <div class="product-cell update-cell">
          <span class="cell-label">Update</span>
          <!-- <span class="update active"
            ><i class="fa-solid fa-pen-to-square"></i
          ></span> -->
          <a href="#" class="update active"
            ><i class="fa-solid fa-pen-to-square"></i
          ></a>
        </div>
        <div class="product-cell">
          <span class="cell-label">Delete:</span>
          <!-- <span class="delete"><i class="fa-solid fa-trash"></i></span> -->
          <a href="#" class="delete"><i class="fa-solid fa-trash"></i></a>
        </div>
      </div>
        `

        productContainer.innerHTML += products

      }

    })
  }

  buildProduct()