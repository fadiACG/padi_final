function addRow() {
    let name = document.getElementById("nameId").value, property = document.getElementById("propertyId").value,
        size = document.getElementById("sizeId").value, i = document.getElementById("propertyTable").rows.length;
    if (!$.isNumeric(size)) {
        alert("Invalid Size. Please enter the correct value.");
        return;
    }

    if (name && property && size) {
        $("#propertyTable>tbody").append("<tr><td>" + i + "</td><td> " + name + "</td><td> " + property + "</td><td>" + size + "</td><td>" +
            "<button type=\"button\" onclick=\"removeRow(this)\" class=\"btn btn-danger\">Delete</button></td></tr>");
    } else {
        alert("Please fill all the required fields.");
    }
}

function removeRow(row) {
    row.closest('tr').remove();
}

function sort_by_name()
{
    $("#propertyTable").tablesorter();
}
