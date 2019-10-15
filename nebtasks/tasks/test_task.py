from nebu.cli.task_extensions import neb_task, NebTask

@neb_task(name='echo_task')
def echo_task():
    """echo back collection id"""
    def collection_action(id, file, resources):
        print(id)

    return NebTask(collection_action=collection_action)
