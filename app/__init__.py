from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from app.database import session, Project

# Cria uma instância do Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html', title="Página Inicial")

@app.route('/projects', methods=['GET'])
def list_projects():
    """Endpoint para listar todos os projetos."""
    projects = session.query(Project).all()
    return render_template('projects.html', projects=projects)

@app.route('/projects/new', methods=['GET'])
def new_project():
    """Renderiza o formulário para cadastrar um novo projeto."""
    return render_template('create_project.html')

@app.route('/projects/<int:project_id>/edit', methods=['GET'])
def edit_project(project_id):
    """Renderiza o formulário para editar um projeto existente."""
    project = session.get(Project, project_id)
    if not project:
        flash('Projeto não encontrado.', 'danger')
        return redirect(url_for('list_projects'))
    return render_template('edit_project.html', project=project)

@app.route('/projects/<int:project_id>', methods=['POST'])
def update_project(project_id):
    """Atualiza um projeto existente."""
    try:
        project = session.get(Project, project_id)
        if not project:
            flash('Projeto não encontrado.', 'danger')
            return redirect(url_for('list_projects'))

        # Atualiza os dados do projeto
        project.code = request.form['code']
        project.title = request.form['title']
        project.description = request.form.get('description', '')

        session.commit()
        flash('Projeto atualizado com sucesso!', 'success')
        return redirect(url_for('list_projects'))
    except Exception as e:
        session.rollback()
        flash(f'Erro ao atualizar o projeto: {e}', 'danger')
        return redirect(url_for('list_projects'))

@app.route('/projects/<int:project_id>/delete', methods=['POST'])
def delete_project(project_id):
    """Exclui um projeto existente."""
    try:
        project = session.get(Project, project_id)
        if not project:
            flash('Projeto não encontrado.', 'danger')
            return redirect(url_for('list_projects'))

        session.delete(project)
        session.commit()
        flash('Projeto excluído com sucesso!', 'success')
        return redirect(url_for('list_projects'))
    except Exception as e:
        session.rollback()
        flash(f'Erro ao excluir o projeto: {e}', 'danger')
        return redirect(url_for('list_projects'))

@app.route('/projects', methods=['POST'])
def create_project():
    """Endpoint para criar um novo projeto."""
    try:
        # Verifica se os dados vêm de um formulário HTML
        if request.form:
            code = request.form['code']
            title = request.form['title']
            description = request.form.get('description', '')
        else:
            # Caso contrário, assume que os dados vêm como JSON
            data = request.json
            code = data['code']
            title = data['title']
            description = data.get('description', '')

        new_project = Project(
            code=code,
            title=title,
            description=description
        )
        session.add(new_project)
        session.commit()
        flash('Projeto criado com sucesso!', 'success')  # Adiciona a mensagem de sucesso
        return redirect(url_for('new_project'))  # Redireciona para o formulário novamente
    except Exception as e:
        session.rollback()
        flash(f'Erro ao criar o projeto: {e}', 'danger')  # Adiciona a mensagem de erro
        return redirect(url_for('new_project'))

if __name__ == '__main__':
    app.run(debug=True)