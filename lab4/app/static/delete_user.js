"use strict"

function fillModal(event) {
    let deleteUrl = event.relatedTarget.dataset.deleteUrl;

    let modalForm = event.target.querySelector("form");
    modalForm.action = deleteUrl;
}

window.onload = function () {
    let deleteModal = document.getElementById("delete-modal");
    deleteModal.addEventListener("show.bs.modal", fillModal);
}
$('#delete-modal').on('show.bs.modal', function(event) {
    var button = $(event.relatedTarget);
    var name = button.data('name');
    var lastName = button.data('last-name');
    var surname = button.data('surname');
    
    var modal = $(this);
    modal.find('.modal-body #user-name').text(name);
    modal.find('.modal-body #user-last-name').text(lastName);
    modal.find('.modal-body #user-surname').text(surname);
    
    var deleteUrl = button.data('delete-url');
    modal.find('#delete-form').attr('action', deleteUrl);
});
