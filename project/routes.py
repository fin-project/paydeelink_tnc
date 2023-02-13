
from flask import render_template, request
from project import app

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('ThankYou.html')

@app.route('/', methods=['GET', 'POST'])
def mpi_redirect():

    print("---header---")
    print(request.headers)
    
    print("------data------")
    appr_code = request.form.get('MPI_APPR_CODE',"")
    rrn = request.form.get('MPI_RRN',"")
    bin = request.form.get('MPI_BIN',"")
    error_code = request.form.get('MPI_ERROR_CODE',"")
    error_desc = request.form.get('MPI_ERROR_DESC',"")
    merc_id = request.form.get('MPI_MERC_ID',"")
    trxn_id = request.form.get('MPI_TRXN_ID',"")
    mac = request.form.get('MPI_MAC',"")
    referral_code = request.form.get('MPI_REFERRAL_CODE',"")    
    
    # Additional data
    eci = request.form.get('MPI_ECI_VALUE',"")    
    challenge_mandated_ind = request.form.get('MPI_CHALLENGE_MANDATED_IND',"")    
    challenge_ind = request.form.get('MPI_CHALLENGE_IND',"")    
    auth_status = request.form.get('MPI_AUTH_STATUS',"")   
    status_reason = request.form.get('MPI_STATUS_REASON',"")   
    status_reason_desc = request.form.get('MPI_STATUS_REASON_DESC',"")
  
    # PAG
    pymt_method = request.form.get('MPI_CUST_PAYMENT_METHOD', "")

    #return Response(result, status=200)
    return render_template('MpiResult.html', appr_code = appr_code, rrn = rrn, bin = bin, 
        error_code = error_code, error_desc = error_desc, merc_id = merc_id, trxn_id = trxn_id, 
        referral_code = referral_code,
        eci = eci, challenge_mandated_ind = challenge_mandated_ind, challenge_ind = challenge_ind,
        status_reason = status_reason, status_reason_desc = status_reason_desc, pymt_method = pymt_method
        )