import click
import os


@click.group()
def cli():
    pass


@click.command()
@click.argument('file_name')
@click.option('--crud', is_flag=True)
def new(file_name, crud):
    crudController = ""
    crudRouter = ""
    if crud:
        crudController = """
    async getAll(req: Request, res: Response){
        const pool = await getPool()
    }
    async getById(req: Request, res: Response){
        const pool = await getPool()
    }
    async create(req: Request, res: Response){
        const pool = await getPool()
    }
    async editById(req: Request, res: Response){
        const pool = await getPool()
    }
    async deleteById(req: Request, res: Response){
        const pool = await getPool()
    }
"""
        crudRouter = """
router.get('/',controller.getAll)
router.get('/:id',controller.getById)
router.post('/',controller.create)
router.put('/:id',controller.editById)
router.delete('/',controller.deleteById)
"""

    files = [
        {
            "route": f'src/controllers/controller-{file_name}.ts',
            "content": f"""import {{ Request, Response }} from 'express'
import {{ getPool }} from '../database'
export class {file_name.title()} {{{crudController}}}"""},
        {
            "route": f'src/interfaces/interface-{file_name}.ts',
            "content": f"export interface i{file_name.title()} {{}}"},
        {
            "route": f'src/routes/{file_name}.ts',
            "content": f"""import {{ Router }} from 'express';
import {{ {file_name.title()} }} from '../controllers/controller-{file_name}'
const controller = new {file_name.title()}()
const router = Router()
{crudRouter}
export default router"""}]

    for a in files:
        if not os.path.exists(os.path.dirname(a['route'])):
            try:
                os.makedirs(os.path.dirname(a['route']))
            except os.error as e:
                print(e)
        f = open(a['route'], 'w')
        f.write(a['content'])


cli.add_command(new)

if __name__ == '__main__':
    cli()
