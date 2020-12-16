// var cart_count = 0;

// if(localStorage.getItem('cart')==null){
//     var cart = {};
//     $("#cart_count")[0].innerText = cart_count 

// }
// else{
//     cart = JSON.parse(localStorage.getItem('cart'))
//     cart_count = Object.keys(cart).length;
//     $("#cart_count")[0].innerText = cart_count 
// }

// $(".cart").click(
//     function (){
//         var name = this.id.toString();
//         if(name != undefined && cart[name]!=null){
//             cart[name] = cart[name] + 1;
//         }
//         else{
//             cart[name]=1;
//         }
//         localStorage.setItem('cart' , JSON.stringify(cart));
//         cart_count = Object.keys(cart).length;
//         $("#cart_count")[0].innerText = cart_count 
//         UpdateCart();
//     }
//     );
    
// function UpdateCart() {
//     for(item in cart){
//         a = item.slice(2);
//     }
// }


// qnt = $("#id_quantity")[0];
$(".proqnt").on("change", function(){
    slugname = $(this).parent().siblings()[0].innerText.toString();
    value = Math.max(0,this.value);
    $.ajax({
        url: '/cart',
        type: 'get',
        data: {
            name : slugname,
            value: value
        },
        success: function(){
            console.log("working");
            location.reload();
        } 
      });

});

