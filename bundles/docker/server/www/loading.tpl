<style>
      .text-no-select {
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
      }
      .trame__loader {
        display: block;
        position: relative;
        left: 50%;
        top: calc(50% - 50px);
        width: 150px;
        height: 150px;
        margin: -75px 0 0 -75px;
        border-radius: 50%;
        border: 10px solid transparent;
        border-top-color: #ac262c;

        -webkit-animation: spin 2s linear infinite; /* Chrome, Opera 15+, Safari 5+ */
        animation: spin 2s linear infinite; /* Chrome, Firefox 16+, IE 10+, Opera */
      }

      .trame__loader:before {
        content: "";
        position: absolute;
        top: 5px;
        left: 5px;
        right: 5px;
        bottom: 5px;
        border-radius: 50%;
        border: 10px solid transparent;
        border-top-color: #258e44;

        -webkit-animation: spin 3s linear infinite; /* Chrome, Opera 15+, Safari 5+ */
        animation: spin 3s linear infinite; /* Chrome, Firefox 16+, IE 10+, Opera */
      }

      .trame__loader:after {
        content: "";
        position: absolute;
        top: 20px;
        left: 20px;
        right: 20px;
        bottom: 20px;
        border-radius: 50%;
        border: 10px solid transparent;
        border-top-color: #1c4678;

        -webkit-animation: spin 1.5s linear infinite; /* Chrome, Opera 15+, Safari 5+ */
        animation: spin 1.5s linear infinite; /* Chrome, Firefox 16+, IE 10+, Opera */
      }

      .trame__message {
        position: absolute;
        text-align: center;
        width: 100%;
        top: calc(50% + 50px);
        font-size: 200%;
        user-select: none;
      }

      @-webkit-keyframes spin {
        0% {
          -webkit-transform: rotate(0deg); /* Chrome, Opera 15+, Safari 3.1+ */
          -ms-transform: rotate(0deg); /* IE 9 */
          transform: rotate(0deg); /* Firefox 16+, IE 10+, Opera */
        }
        100% {
          -webkit-transform: rotate(360deg); /* Chrome, Opera 15+, Safari 3.1+ */
          -ms-transform: rotate(360deg); /* IE 9 */
          transform: rotate(360deg); /* Firefox 16+, IE 10+, Opera */
        }
      }
      @keyframes spin {
        0% {
          -webkit-transform: rotate(0deg); /* Chrome, Opera 15+, Safari 3.1+ */
          -ms-transform: rotate(0deg); /* IE 9 */
          transform: rotate(0deg); /* Firefox 16+, IE 10+, Opera */
        }
        100% {
          -webkit-transform: rotate(360deg); /* Chrome, Opera 15+, Safari 3.1+ */
          -ms-transform: rotate(360deg); /* IE 9 */
          transform: rotate(360deg); /* Firefox 16+, IE 10+, Opera */
        }
      }
</style>
<div style="position:absolute;top:0;left:0;width:100%;height:100%;z-index:1000;">
  <div class="trame__loader"></div>
  <div class="trame__message">Loading...</div>
</div>
