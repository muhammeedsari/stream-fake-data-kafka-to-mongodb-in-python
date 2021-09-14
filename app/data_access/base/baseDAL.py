from typing import TypeVar, Generic, List

T = TypeVar('T')

class BaseDal(Generic[T]):
    def get(self, filter:any):
        query = T.objects(filter)
        return query

    def get_all(self):
        count = T.objects.count()
        return count


    def delete(self, filter:any):
        mongodb_context = T.objects(filter)
        mongodb_context.delete()


    def update(self, filter:any, update_object:any):
        mongodb_context = T.objects(filter)
        mongodb_context.update(update_object)


    def add(self, mongodb_context:T, tag_list:List[str]):
        mongodb_context.tags = tag_list
        mongodb_context.save()