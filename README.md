# redis-to-instapaper
Subscribe to a Redis channel, saving hyperlinks received through it to an Instapaper account

# What is redis-to-instapaper?

redis-to-instapaper is a Python application which will subscribe to a Redis channel, posting hyperlinks received through the channel to an Instapaper account.

# How to use this image

This redis-to-instapaper container must be linked to a redis container (which must have the alias `redis`). Instapaper account credentials must be supplied as environment variables. 

    docker run --name redis-to-instapaper --link redis:redis -e USERNAME='username' -e PASSWORD='password' -d digmore/redis-to-instapaper

**NOTE**: The default channel name is `instapaper`. See the `CHANNEL` environment variable below to override this.

## Configuration

ENVIRONMENT VARIABLES (only available with `docker run`)

 * `USERNAME` - Set the username for the Instapaper account (required)
 * `PASSWORD` - Set the password for the Instapaper account (optional)
 * `CHANNEL` - Set the Redis channel name to subscribe to (option, defaults to `instapaper`)

# User Feedback

## Issues

If you want to contact me with questions, or to report problems with this image,
please raise a [GitHub issue](https://github.com/digmore/redis-to-instapaper/issues)

