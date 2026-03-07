import re

with open('slides.md', 'r') as f:
    content = f.read()

new_block = """<div class="ancestry-container" style="margin-top: -30px;">
<div class="ancestry-flow" style="transform: scale(0.53);">
<!-- Row 0: Education -->
<div class="a-row" style="width: 100%; justify-content: flex-end;">
<div class="a-node a-fade-1">
<img class="a-avatar bg-white-logo" src="https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=http://osmania.ac.in&size=128">
<div class="a-name">Osmania University</div>
<div class="a-org">Education</div>
</div>
<div class="a-arrow a-fade-2"><i class="fa-solid fa-arrow-right"></i></div>
<div class="a-node a-fade-3">
<img class="a-avatar bg-white-logo" src="https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=http://uohyd.ac.in&size=128">
<div class="a-name">University of Hyderabad</div>
<div class="a-org">Education</div>
</div>
<div class="a-arrow a-fade-4"><i class="fa-solid fa-arrow-right"></i></div>
<div class="a-node a-fade-5">
<img class="a-avatar bg-white-logo" src="https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=http://uri.edu&size=128">
<div class="a-name">University of Rhode Island</div>
<div class="a-org">Education</div>
</div>
</div>

<div class="a-turn a-fade-6" style="align-self: flex-end; margin-right: 35px;">
<div class="a-arrow"><i class="fa-solid fa-arrow-down"></i></div>
</div>

<!-- Row 1: Early Career -->
<div class="a-row">
<div class="a-node a-fade-13">
<img class="a-avatar bg-white-logo" src="https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=http://prudential.com&size=128">
<div class="a-name">Prudential</div>
<div class="a-org">Director</div>
</div>
<div class="a-arrow a-fade-12"><i class="fa-solid fa-arrow-left"></i></div>
<div class="a-node a-fade-11">
<img class="a-avatar bg-white-logo" src="https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=http://dell.com&size=128">
<div class="a-name">Dell EMC</div>
<div class="a-org">Analytics Lead</div>
</div>
<div class="a-arrow a-fade-10"><i class="fa-solid fa-arrow-left"></i></div>
<div class="a-node a-fade-9">
<img class="a-avatar bg-white-logo" src="https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=http://mit.edu&size=128">
<div class="a-name">MIT</div>
<div class="a-org">PostDoc</div>
</div>
<div class="a-arrow a-fade-8"><i class="fa-solid fa-arrow-left"></i></div>
<div class="a-node a-fade-7">
<img class="a-avatar bg-white-logo" src="https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=http://harvard.edu&size=128">
<div class="a-name">Harvard</div>
<div class="a-org">PostDoc</div>
</div>
</div>

<div class="a-turn a-fade-14" style="align-self: flex-start; margin-left: 35px;">
<div class="a-arrow"><i class="fa-solid fa-arrow-down"></i></div>
</div>

<!-- Row 2: Leadership -->
<div class="a-row">
<div class="a-node a-fade-15">
<img class="a-avatar bg-white-logo" src="https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=http://dnb.com&size=128">
<div class="a-name">Dun & Bradstreet</div>
<div class="a-org">Sr Director</div>
</div>
<div class="a-arrow a-fade-16"><i class="fa-solid fa-arrow-right"></i></div>
<div class="a-node a-fade-17">
<img class="a-avatar bg-white-logo" src="https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=http://db.com&size=128">
<div class="a-name">Deutsche Bank</div>
<div class="a-org">Head of Data Science</div>
</div>
<div class="a-arrow a-fade-18"><i class="fa-solid fa-arrow-right"></i></div>
<div class="a-node highlight a-fade-19">
<img class="a-avatar bg-white-logo" src="images/powerlytics.png?v=1">
<div class="a-name">Powerlytics</div>
<div class="a-org">Chief Data & Analytics Officer</div>
</div>
<div class="a-arrow a-fade-20"><i class="fa-solid fa-arrow-right"></i><span class="a-relation-text" style="top: -20px;">Current</span></div>
<div class="a-node highlight a-fade-21">
<img class="a-avatar bg-white-logo" src="images/chari.jpg" style="padding: 0; object-fit: cover;">
<div class="a-name">Narahara Chari Dingari, Ph.D.</div>
<div class="a-org">CDAO & Board Member</div>
</div>
</div>

<div class="a-turn a-fade-22" style="align-self: center; transform: translateX(110px); margin-top: -10px; margin-bottom: -10px;">
<div class="a-arrow"><i class="fa-solid fa-arrow-down"></i><span class="a-relation-text">Advisory</span></div>
</div>

<!-- Row 3: Advisory -->
<div class="a-row">
<div class="a-node" style="width: 220px; opacity: 0; visibility: hidden;"></div>
<div class="a-arrow" style="opacity: 0; visibility: hidden;"><i class="fa-solid fa-arrow-right"></i></div>
<div class="a-node" style="width: 220px; opacity: 0; visibility: hidden;"></div>
<div class="a-arrow" style="opacity: 0; visibility: hidden;"><i class="fa-solid fa-arrow-right"></i></div>
<div class="a-node a-fade-23">
<img class="a-avatar bg-white-logo" src="https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=http://wpi.edu&size=128">
<div class="a-name">WPI</div>
<div class="a-org">Adjunct Professor</div>
</div>
<div class="a-arrow a-fade-24"><i class="fa-solid fa-plus"></i></div>
<div class="a-node a-fade-25">
<img class="a-avatar bg-white-logo" src="https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=http://datacamp.com&size=128">
<div class="a-name">DataCamp</div>
<div class="a-org">Advisory Board</div>
</div>
<div class="a-arrow a-fade-26"><i class="fa-solid fa-plus"></i></div>
<div class="a-node a-fade-27">
<img class="a-avatar bg-white-logo" src="https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=http://fullsail.edu&size=128">
<div class="a-name">Full Sail Univ</div>
<div class="a-org">Board Member</div>
</div>
</div>
</div>
</div>"""

pattern = r'<div class="ancestry-container".*?</div>\n</div>\n</div>'
new_content = re.sub(pattern, new_block, content, flags=re.DOTALL)

with open('slides.md', 'w') as f:
    f.write(new_content)
