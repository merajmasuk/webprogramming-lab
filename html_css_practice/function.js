function myFunction() {
	let rows=document.getElementById("myTable").rows.length;

	for (let i=0; i<rows; i++)
	{
		let j = 1;
		
		for ( ; j<4; j++)
		{
			if (i % 2 != 0 || i == 0){
				document.getElementById("myTable").rows[i].cells[j].style.fontFamily='acumin-pro';
				document.getElementById("myTable").rows[i].cells[j].style.background='silver';
			}
			else {
				document.getElementById("myTable").rows[i].cells[j-1].style.fontFamily='acumin-pro';
				document.getElementById("myTable").rows[i].cells[j-1].style.background='silver';
			}
		}
		for ( ; j<6; j++){
			if (i % 2 != 0 || i == 0){
				document.getElementById("myTable").rows[i].cells[j].style.fontFamily='helvetica';
				document.getElementById("myTable").rows[i].cells[j].style.background='teal';
			}
			else {
				document.getElementById("myTable").rows[i].cells[j-1].style.fontFamily='helvetica';
				document.getElementById("myTable").rows[i].cells[j-1].style.background='teal';
			}
		}
		for ( ; j<7; j++){
			if (i % 2 != 0 || i == 0){
				document.getElementById("myTable").rows[i].cells[j].style.fontFamily='chaletcomprime';
				document.getElementById("myTable").rows[i].cells[j].style.background='lightblue';
			}
			else {
				document.getElementById("myTable").rows[i].cells[j-1].style.fontFamily='chaletcomprime';
				document.getElementById("myTable").rows[i].cells[j-1].style.background='lightblue';
			}
		}
	} 
}
	
function imgShow() {
  document.getElementById('preview-01-img').style.opacity = 1;
}

function imgHide() {
  document.getElementById('preview-01-img').style.opacity = 0;
}