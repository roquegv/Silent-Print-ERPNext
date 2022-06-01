// How to extend page function: https://discuss.erpnext.com/t/pos-custom-script-in-point-of-sale/29554/15
frappe.require('assets/js/point-of-sale.min.js', function() {
    erpnext.PointOfSale.PastOrderSummary.prototype.print_receipt =  function(parent) {
        const frm = this.events.get_frm();
        var printService = new WebSocketPrinter();
        frappe.call({
            method: 'silent_print.utils.print_format.create_pdf',
            args: {
                doctype: frm.doc.doctype,
                name: frm.doc.name,
                silent_print_format: frm.pos_print_format,
            },
            callback: (r) => {
                if(r.message){
                    printService.submit({
                        'type': r.message.print_type,
                        'url': 'file.pdf',
                        'file_content': r.message.pdf_base64
                    });
                } else {
                    const frm = this.events.get_frm();
                    frappe.utils.print(
                        this.doc.doctype,
                        this.doc.name,
                        frm.pos_print_format,
                        this.doc.letter_head,
                        this.doc.language || frappe.boot.lang
                    );
                }
            }
        })
    }
})

var WebSocketPrinter = function (options) {
    var defaults = {
        url: "ws://127.0.0.1:12212/printer",
        onConnect: function () {
        },
        onDisconnect: function () {
        },
        onUpdate: function () {
        },
    };

    var settings = Object.assign({}, defaults, options);
    var websocket;
    var connected = false;

    var onMessage = function (evt) {
        settings.onUpdate(evt.data);
    };

    var onConnect = function () {
        connected = true;
        settings.onConnect();
    };

    var onDisconnect = function () {
        connected = false;
        settings.onDisconnect();
        reconnect();
    };
    
    var onError = function () {
        if (frappe.whb == undefined){
            frappe.msgprint("No se pudo establecer conexión con la impresora. Favor verificar que el <a href='https://github.com/imTigger/webapp-hardware-bridge' target='_blank'>WebApp Hardware Bridge</a> esté ejecutándose.")
            frappe.whb = true
        }
    };

    var connect = function () {
        websocket = new WebSocket(settings.url);
        websocket.onopen = onConnect;
        websocket.onclose = onDisconnect;
        websocket.onmessage = onMessage;
        websocket.onerror = onError;
    };

    var reconnect = function () {
        connect();
    };

    this.submit = function (data) {
        if (Array.isArray(data)) {
            data.forEach(function (element) {
                websocket.send(JSON.stringify(element));
            });
        } else {
            websocket.send(JSON.stringify(data));
        }
    };

    this.isConnected = function () {
        return connected;
    };

    connect();
}