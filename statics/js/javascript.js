const plus = document.querySelector('#add-item');
const formGroup = document.querySelector('#form-groupx');
const removeItem = document.querySelector('#remove-item')

loadEventListener();


function loadEventListener(){

    plus.addEventListener('click',addRow)
    removeItem.addEventListener('click',removeRow)


}

function addRow(e){

    let x = document.createElement('div');
    x.innerHTML='<input name="rdate" type="date" class=" form-group col-md-1" /><input name="hour" type="time" class="form-group col-md-1 " /><select name="status" class="form-group col-md-1 "><option value="1 ">اولیه</option><option value="2 ">ثانویه</option><option value="3 ">در اختیار </option></select><input name="billid" type=" " class="form-group col-md-1" placeholder="شماره قبض" /><input name="tankid" type=" " class="form-group col-md-1" placeholder="شماره مخزن" /><input name="size" type=" " class="form-group col-md-1" placeholder="اندازه مخزن" /><input name="temprature" type=" " class="form-group col-md-1" placeholder="دما" /><input name="water" type=" " class="form-group col-md-1" placeholder="آب" /><select name="refinery" class="form-group col-md-1 "><option value="Kerosine ">نفت سفید</option><option value="Gasoil ">گازوئیل</option><option value="Motor Spirite ">بنزین</option></select><input name="specweight" type=" " class="form-group col-md-1" placeholder="وزن" /><input name="envtemp" type=" " class="form-group col-md-1" placeholder="دمای محیط" />';
    x.setAttribute('class','form-itemsx')
    formGroup.appendChild(x);
    e.preventDefault();

}

function removeRow(e){

    let y= formGroup.lastChild;
    y.remove();
}

