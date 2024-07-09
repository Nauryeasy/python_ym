from python_ym import api_objects


class WarehousesMixin:

    def get_warehouses(self) -> list[api_objects.Warehouse]:

        result = self._get_request_get(url=self._api_config.get_warehouse_endpoint(), path_params={})['result']['warehouses']

        warehouses = []

        for warehouse in result:
            warehouses.append(api_objects.Warehouse(warehouse))

        return warehouses