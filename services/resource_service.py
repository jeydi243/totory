



class ResourceService:
    def get(self) ->list[any]:
        try:
            return Resources.objects.values_list()
        except TypeError as te:
            print("TypeError: ", te)
        except ValueError as ve:
            print("ValueError: ", ve)
        except BaseException as e:
            print(f"{e}")