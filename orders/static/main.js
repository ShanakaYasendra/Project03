
        var id =null;
        var numb= null;
        
      
        var toppinglist=[];
    $('a[href="#myModal"]').on('click',function(){
    id = $(this).attr('data-name');
    price=$(this).attr('data-price');
    
  
    console.log(id)
            checkNoTopping(id)
        $('h4[name="modal-title"]').append(id);
        document.getElementById("pizzaname").innerHTML=id;
        document.getElementById("price").innerHTML=price;
        
        });


        function   validatefunction(id){
            var check= document.querySelectorAll('input[name="topping"]:checked')
            console.log(check)
            if(check.length != parseInt(numb))
            {
                alert("Pleae select " +numb+"  topping")

                return false;
            
            }
            else{
                return true;
            }
        
        }


        function checkNoTopping(id){
        
        numb = id.match(/\d/g);
        numb = numb.join("");
        console.log(numb)
    };

    function getValueofCheckBox()
    {
        var selected= new Array();
        var checkbox= document.getElementById("toppings");
        var selectcheck= checkbox.getElementsByTagName("input");
        
        for(var i=0; i<selectcheck.length; i++)
        {
        
            if(selectcheck[i].checked)
            {
                if(validatefunction()==true)
                {
                selected.push(selectcheck[i].value)
                }
                else{
                    selectcheck[i].checked= false;
                }
            
            
            }
        

            
        }
        document.getElementById("displayTopping").innerHTML=selected
    }
        // call onload or in script segment below form
       function request_access($this){
        var Active_category= $("#Active_category_model").text();
        console.log(Active_category)
        var price= $("#price").text();
        console.log(price)
        var topping= $("#displayTopping").text();
        console.log(topping)
        console.log("button clicked");
    

        var request_data = $this.id;
        console.log("data: " + request_data);
        $.ajax({
            url: '/orderpizza/'+Active_category+'/'+id+'/'+price+'/'+topping,
            
            success : function(data) {
                console.log('request Success')
            }
        })

    }
 
