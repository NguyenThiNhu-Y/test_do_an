css = '''
<style>
[data-testid="stAppViewContainer"]{
background: #fccb90;
background: -webkit-linear-gradient(to bottom right, rgba(252, 203, 144, 1), rgba(213, 126, 235, 1));
background: linear-gradient(to bottom right, rgba(252, 203, 144, 1), rgba(213, 126, 235, 1))
}
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
.mask-custom {
background: rgba(24, 24, 16, .2);
border-radius: 2em;
backdrop-filter: blur(15px);
border: 2px solid rgba(255, 255, 255, 0.05);
background-clip: padding-box;
box-shadow: 10px 10px 10px rgba(46, 54, 68, 0.03);
}
.auto-width {
display: inline-block;
width: fit-content;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''


msg_user = '''
<li class="d-flex mb-4 float-right">
    <div class="card mask-custom auto-width">
        <div class="card-header d-flex justify-content-between p-3 "
            style="border-bottom: 1px solid rgba(255,255,255,.3);">
            <p class="text-light small mb-0"><i class="far fa-clock"></i> 13 mins ago</p>
            <p class="fw-bold mb-0 ml-3">user</p>
        </div>
        <div class="card-body">
            <p class="mb-0 text-right">
                {{MSG_user}}
            </p>
        </div>
    </div>
    <img src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/avatar-5.webp" alt="avatar"
        class="rounded-circle d-flex align-self-start ms-3 shadow-1-strong ml-3" width="60">
</li>
'''

msg_bot = '''
<li class="d-flex mb-4">
    <img src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/avatar-6.webp" alt="avatar"
        class="rounded-circle d-flex align-self-start me-3 shadow-1-strong mr-3" width="60">
    <div class="card mask-custom auto-width">
        <div class="card-header d-flex justify-content-between p-3"
            style="border-bottom: 1px solid rgba(255,255,255,.3);">
            <p class="fw-bold mb-0 mr-3">bot</p>
            <p class="text-light small mb-0"><i class="far fa-clock"></i> 13 mins ago</p>
        </div>
        <div class="card-body">
            <p class="mb-0">
                {{MSG_bot}}
            </p>
        </div>
    </div>
</li>
'''

test_css = '''
    <ul class="list-unstyled text-white">
        
        
        <li class="mb-3">
            <div class="form-outline form-white">
                <textarea class="form-control" id="textAreaExample3" rows="4"></textarea>
                <label class="form-label" for="textAreaExample3">Message</label>
            </div>
        </li>
        <button type="button" class="btn btn-light btn-lg btn-rounded float-end">Send</button>
    </ul>

'''
