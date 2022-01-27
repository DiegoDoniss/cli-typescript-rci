#! C:\Users\diego\AppData\Local\Programs\Python\Python310\ python
import click
import os

@click.group()
def cli():
    pass

@click.command()
@click.argument('file_name')
def new(file_name):
    
    files = [{"route":f'src/controllers/controller-{file_name}.ts', "content":f"""import {{ Request, Response }} from 'express'
import {{ getPool }} from '../database'
export class {file_name.title()} {{}}"""},{"route":f'src/interfaces/interface-{file_name}.ts', "content":f"export interface i{file_name.title()} {{}}"},{"route":f'src/routes/{file_name}.ts',"content":f"""import {{ Router }} from 'express';
import {{ {file_name.title()} }} from '../controllers/controller-{file_name}'
const controller = new {file_name.title()}()
const router = Router()
export default router"""}]

    for a in files:
        if not os.path.exists(os.path.dirname(a['route'])):
            try:
                os.makedirs(os.path.dirname(a['route']))
            except os.error as e:
                print(e)
        f=open(a['route'], 'w')
        f.write(a['content'])

cli.add_command(new)

if __name__ == '__main__':
    cli()