from decimal import Decimal
from django.conf import settings
from shop.models import Producto

class Cart:
    def __init__(self, request):
        """
            Inicializar el carrito.
        """
        
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # guardar un carrito vacío en la sesión
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
            Iterar los items del carrito y obtener los productos 
            de la base de datos.
        """
        producto_ids = self.cart.keys()
        # Obtener los objetos del producto y agregarlos al carrito.
        productos = Producto.objects.filter(id__in=producto_ids)
        cart = self.cart.copy()
        for producto in productos:
            cart[str(producto.id)]['producto'] = producto
        for item in cart.values():
            item['precio'] = int(item['precio'])
            item['total_precio'] = item['precio'] * item['cantidad']
            yield item

    def __len__(self):
        """
            Cuenta todos los artículos en el carrito.
        """
        return sum(item['cantidad'] for item in self.cart.values())

    def agregar(self, producto, cantidad=1, anular_cantidad=False):  
        """
            Añade un producto al carrito o actualiza su cantidad.
        """
        producto_id = str(producto.id)
        if producto_id not in self.cart:
            self.cart[producto_id] = {'cantidad': 0,
                                     'precio': str(producto.precio)}
        if anular_cantidad:
            self.cart[producto_id]['cantidad'] = cantidad
        else:
            self.cart[producto_id]['cantidad'] += cantidad
        self.guardar()

    def guardar(self):
        #marca la sesión como "modificada" para asegurar de que se guarde
        self.session.modified = True  

    def remover(self, producto):
        """
            Remueve un producto del carrito.
        """
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.guardar()

    def limpiar(self):
        # remueve el carrito de la sesion
        del self.session[settings.CART_SESSION_ID]
        self.guardar()

    def get_total_precio(self):
        return sum(int(item['precio']) * item['cantidad'] for item in self.cart.values())