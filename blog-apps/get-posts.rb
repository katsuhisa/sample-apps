require 'json'
require 'sinatra'

posts = [
    {title: "First Post", content: "This is the first post."},
    {title: "Second Post", content: "This is the second post."}
]

get '/get-posts' do
    content_type :json
    posts.to_json
end