from invoke import task

@task
def start(ctx):
	ctx.run("python3 ../thing.py", pty=True)
